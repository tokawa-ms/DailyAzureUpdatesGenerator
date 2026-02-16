#!/usr/bin/env python3
"""
Application to read Azure Updates RSS feed and summarize updates within a specified timeframe using Azure OpenAI
(DefaultAzureCredential authentication version)

Authentication methods:
- Local environment: Azure CLI credentials (must be logged in with az login)
- Cloud environment (AZURE_TENANT_ID + AZURE_CLIENT_ID + AZURE_CLIENT_SECRET set): Service principal authentication
- OIDC environment (AZURE_TENANT_ID + AZURE_CLIENT_ID + OIDC context): Workload Identity authentication
- Cloud environment (AZURE_TENANT_ID + AZURE_CLIENT_ID only set): Managed ID authentication

Environment Variables:
- AOAI_ENDPOINT: Azure OpenAI endpoint
- DEPLOYMENT: Azure OpenAI deployment name
- API_VER: Azure OpenAI API version
- CHECK_HOURS: Target check period in hours (default: 24 hours)
- AZURE_TENANT_ID: Azure AD tenant ID (optional, for cloud environment)
- AZURE_CLIENT_ID: Client ID (optional, for cloud environment)
- AZURE_CLIENT_SECRET: Client secret (optional, for service principal authentication)
"""

import os
import sys
import logging
import argparse
from datetime import datetime, timedelta, timezone
from typing import List, Dict, Optional
import json
import time
import re
from email.utils import parsedate_to_datetime
from urllib.parse import urlparse, parse_qs

# Third-party libraries
from dotenv import load_dotenv

load_dotenv()

import feedparser
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Azure Identity library
from azure.identity import DefaultAzureCredential
from azure.core.credentials import TokenCredential

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("azure_updates.log", encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
logger = logging.getLogger(__name__)


def is_truthy_env(var_name: str) -> bool:
    return os.getenv(var_name, "").strip().lower() in {"1", "true", "yes", "on"}


if not is_truthy_env("ENABLE_AZURE_SDK_LOG"):
    logging.getLogger("azure").setLevel(logging.WARNING)
    logging.getLogger("azure.identity").setLevel(logging.WARNING)
    logging.getLogger("azure.core.pipeline.policies.http_logging_policy").setLevel(
        logging.WARNING
    )


class AzureOpenAIClient:
    """Azure OpenAI client (DefaultAzureCredential authentication)"""

    # Scope for Azure OpenAI / Azure Cognitive Services
    _COGNITIVE_SERVICES_SCOPE = "https://cognitiveservices.azure.com/.default"

    def __init__(
        self,
        endpoint: str,
        credential: TokenCredential,
        deployment: str,
        api_version: str,
    ):
        """
        Initialize Azure OpenAI client (DefaultAzureCredential authentication)

        Args:
            endpoint: Azure OpenAI endpoint
            credential: Azure Identity TokenCredential (DefaultAzureCredential, etc.)
            deployment: Deployment name
            api_version: API version
        """
        self.endpoint = endpoint.rstrip("/")
        self.credential = credential
        self.deployment = deployment
        self.api_version = api_version

        # Token cache
        self._cached_token = None

        # HTTP session configuration with retry functionality
        self.session = requests.Session()
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

        # Set only Content-Type header (authentication token is added per request)
        self.session.headers.update({"Content-Type": "application/json"})

        logger.info(
            "Azure OpenAI client initialized (DefaultAzureCredential authentication)"
        )

    def _get_token(self) -> str:
        """
        Retrieve Azure AD token (with cache and auto-refresh)

        Returns:
            Bearer token string
        """
        # Return cached token if still valid
        if self._cached_token and self._cached_token.expires_on > time.time() + 300:
            return self._cached_token.token

        # Retrieve new token
        logger.info("Retrieving Azure AD token...")
        self._cached_token = self.credential.get_token(self._COGNITIVE_SERVICES_SCOPE)
        logger.info("Azure AD token retrieved")
        return self._cached_token.token

    def _get_auth_headers(self) -> Dict[str, str]:
        """
        Generate authentication headers

        Returns:
            Authentication header dictionary containing Bearer token
        """
        token = self._get_token()
        return {"Authorization": f"Bearer {token}"}

    def summarize_update(
        self,
        title: str,
        description: str,
        link: str,
        api_details: Optional[Dict] = None,
    ) -> Optional[str]:
        """
        Summarize Azure Update in English

        Args:
            title: Update title
            description: Update details
            link: Update link
            api_details: Detailed information retrieved from API (optional)

        Returns:
            Summary text (None on failure)
        """
        try:
            url = f"{self.endpoint}/openai/deployments/{self.deployment}/chat/completions?api-version={self.api_version}"

            # Use API information in details mode
            content_source = "RSS"
            actual_title = title
            actual_content = description

            if api_details:
                content_source = "API"
                # Use API title if available
                if api_details.get("api_title"):
                    actual_title = api_details["api_title"]

                # Use API content if available
                if api_details.get("api_content"):
                    actual_content = api_details["api_content"]

                logger.info(
                    f"Using {content_source} information for summary: {actual_title[:50]}..."
                )

            # Create prompt
            prompt = f"""
Please provide a concise English summary of the following Azure Update for technical professionals. Include important points for developers and IT professionals.

Title: {actual_title}

Details: {actual_content}

Link: {link}

Please create the summary in the following format:
- What was updated
- Key changes or new features
- Target audience affected
- Important notes if any

Keep the summary concise, approximately 200 words.

Data source: Using {content_source} data
"""

            payload = {
                "messages": [
                    {
                        "role": "system",
                        "content": "You are an Azure expert. You summarize Azure Update content clearly in English for technical professionals.",
                    },
                    {"role": "user", "content": prompt},
                ],
                "max_tokens": 500,
                "temperature": 0.3,
                "top_p": 0.95,
            }

            response = self.session.post(
                url, json=payload, headers=self._get_auth_headers(), timeout=30
            )
            response.raise_for_status()

            result = response.json()

            if "choices" in result and len(result["choices"]) > 0:
                summary = result["choices"][0]["message"]["content"].strip()
                logger.info(
                    f"Summary completed ({content_source}): {actual_title[:50]}..."
                )
                return summary
            else:
                logger.error("Received unexpected response format")
                return None

        except requests.exceptions.RequestException as e:
            logger.error("API request error occurred")
            return None
        except Exception as e:
            logger.error("Summary processing error occurred")
            return None

    def generate_detailed_summary(
        self, title: str, content: str, link: str
    ) -> Optional[str]:
        """
        Generate detailed summary for details mode (within 500 words)

        Args:
            title: Update title
            content: Update detailed content
            link: Update link

        Returns:
            Detailed summary text (None on failure)
        """
        try:
            url = f"{self.endpoint}/openai/deployments/{self.deployment}/chat/completions?api-version={self.api_version}"

            # Create prompt for detailed summary
            prompt = f"""
Please provide a comprehensive technical explanation of the following Azure Update in English for IT professionals.
You are given the role of generating reports. There is no need for a human response to instructions. Generate a calm and detailed summary sentence.

Title: {title}

Detailed Content: {content}

Link: {link}

Please explain in detail from the following perspectives:
- Background and purpose of the update
- Specific features and detailed changes
- Technical mechanisms and implementation methods
- Use cases and application scenarios
- Important considerations and limitations
- Integration with related Azure services

Use appropriate technical terminology to ensure clarity for engineers.
Generate the summary solely from the provided information, and do not speculate or infer any update details beyond what is given.

Provide detailed information within 500 words that will be useful for technical professionals when actually utilizing this update.
"""

            payload = {
                "messages": [
                    {
                        "role": "system",
                        "content": "You are an Azure expert. You provide detailed explanations of Azure Updates in English for technical professionals. Provide practical and specific information.",
                    },
                    {"role": "user", "content": prompt},
                ],
                "max_tokens": 800,
                "temperature": 0.3,
                "top_p": 0.95,
            }

            response = self.session.post(
                url, json=payload, headers=self._get_auth_headers(), timeout=30
            )
            response.raise_for_status()

            result = response.json()

            if "choices" in result and len(result["choices"]) > 0:
                detailed_summary = result["choices"][0]["message"]["content"].strip()
                logger.info(f"Detailed summary completed: {title[:50]}...")
                return detailed_summary
            else:
                logger.error("Received unexpected response format for detailed summary")
                return None

        except requests.exceptions.RequestException as e:
            logger.error("API request error occurred for detailed summary")
            return None
        except Exception as e:
            logger.error("Detailed summary processing error occurred")
            return None

    def __del__(self):
        """Resource cleanup"""
        if hasattr(self, "session"):
            self.session.close()


class AzureUpdatesProcessor:
    """Azure Updates RSS feed processing class"""

    # Multiple Azure Updates RSS URLs to try
    RSS_URLS = [
        "https://www.microsoft.com/releasecommunications/api/v2/azure/rss",
        "https://azurecomcdn.azureedge.net/en-us/updates/feed/",
        "https://azure.microsoft.com/en-us/updates/feed/",
    ]

    # Azure Updates API base URL
    AZURE_UPDATES_API_BASE = (
        "https://www.microsoft.com/releasecommunications/api/v2/azure/"
    )

    def __init__(
        self,
        openai_client: AzureOpenAIClient,
        check_hours: int = 24,
        details_mode: bool = False,
    ):
        """
        Initialize processor

        Args:
            openai_client: Azure OpenAI client
            check_hours: Target check period in hours
            details_mode: Details mode (retrieve detailed information from API)
        """
        self.openai_client = openai_client
        self.check_hours = check_hours
        self.details_mode = details_mode
        self.cutoff_time = datetime.now(timezone.utc) - timedelta(hours=check_hours)

        logger.info(f"Target check period: within {check_hours} hours")
        logger.info(f"Cutoff time: {self.cutoff_time}")
        logger.info(f"Details mode: {'Enabled' if details_mode else 'Disabled'}")

        # Initialize HTTP session for API access
        self.api_session = self._create_api_session()

    def _create_api_session(self) -> requests.Session:
        """
        Create HTTP session for Azure Updates API access

        Returns:
            Configured HTTP session
        """
        session = requests.Session()

        # Retry strategy
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("http://", adapter)
        session.mount("https://", adapter)

        # Browser spoofing header configuration
        session.headers.update(
            {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                "Accept": "application/json, text/plain, */*",
                "Accept-Language": "en-US,en;q=0.9",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive",
                "Cache-Control": "no-cache",
                "Pragma": "no-cache",
                "Referer": "https://azure.microsoft.com/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
            }
        )

        logger.debug("Initialized HTTP session for Azure Updates API")
        return session

    def extract_update_id(self, link: str) -> Optional[str]:
        """
        Extract update ID from Azure Updates link

        Args:
            link: Azure Updates link

        Returns:
            Update ID (None if cannot extract)
        """
        try:
            # Parse URL
            parsed_url = urlparse(link)

            # Get id from query parameters
            query_params = parse_qs(parsed_url.query)
            if "id" in query_params and query_params["id"]:
                update_id = query_params["id"][0]
                logger.debug(
                    f"Successfully extracted update ID: {update_id} from {link}"
                )
                return update_id

            # Fallback: extract numbers from URL path
            path_match = re.search(r"/(\d+)/?$", parsed_url.path)
            if path_match:
                update_id = path_match.group(1)
                logger.debug(f"Extracted update ID from path: {update_id} from {link}")
                return update_id

            logger.warning(f"Could not extract update ID: {link}")
            return None

        except Exception as e:
            logger.error(f"Update ID extraction error: {link} - {e}")
            return None

    def fetch_update_details(self, update_id: str) -> Optional[Dict]:
        """
        Retrieve detailed information from Azure Updates API

        Args:
            update_id: Update ID

        Returns:
            Detailed information dictionary (None on retrieval failure)
        """
        try:
            api_url = f"{self.AZURE_UPDATES_API_BASE}{update_id}"
            logger.info(f"Retrieving API detailed information: {api_url}")

            response = self.api_session.get(api_url, timeout=30)
            response.raise_for_status()

            # Log response details
            logger.debug(f"API HTTP status: {response.status_code}")
            logger.debug(
                f"API Content-Type: {response.headers.get('Content-Type', 'Unknown')}"
            )
            logger.debug(f"API response length: {len(response.content)} bytes")

            # Parse as JSON
            data = response.json()

            # Calculate data size information
            json_str = json.dumps(data, ensure_ascii=False) if data else "{}"
            char_count = len(json_str)
            byte_count = len(json_str.encode("utf-8"))

            logger.info(
                f"Successfully retrieved API detailed information: {update_id} ({char_count} chars, {byte_count} bytes)"
            )
            logger.debug(
                f"API response structure: {list(data.keys()) if isinstance(data, dict) else type(data)}"
            )

            return data

        except requests.exceptions.RequestException as e:
            logger.error(
                f"HTTP error in API detailed information retrieval: {update_id} - {type(e).__name__}: {e}"
            )
            return None
        except json.JSONDecodeError as e:
            logger.error(
                f"JSON parsing error in API detailed information: {update_id} - {e}"
            )
            return None
        except Exception as e:
            logger.error(
                f"Unexpected error in API detailed information retrieval: {update_id} - {e}"
            )
            return None

    def enhance_update_with_details(self, update: Dict) -> Dict:
        """
        Enhance update information with detailed API information

        Args:
            update: Basic update information

        Returns:
            Enhanced update information
        """
        if not self.details_mode:
            return update

        # Extract update ID
        update_id = self.extract_update_id(update.get("link", ""))
        if not update_id:
            logger.warning(
                f"Skipping detailed information retrieval (no ID): {update.get('title', 'Unknown')}"
            )
            return update

        # Retrieve API detailed information
        details = self.fetch_update_details(update_id)
        if not details:
            logger.warning(
                f"Failed to retrieve detailed information: {update.get('title', 'Unknown')}"
            )
            return update

        # Enhance update with detailed information
        enhanced_update = update.copy()
        enhanced_update["api_details"] = details
        enhanced_update["update_id"] = update_id

        # Override/enhance existing information with information retrieved from API
        if isinstance(details, dict):
            # Update title
            if "title" in details and details["title"]:
                enhanced_update["api_title"] = details["title"]
                logger.debug(f"Retrieved API title: {details['title']}")

            # Update content
            if "content" in details and details["content"]:
                enhanced_update["api_content"] = details["content"]
                logger.debug(
                    f"Retrieved API content: {len(details['content'])} characters"
                )

            # Update publication date
            if "publishedDateTime" in details and details["publishedDateTime"]:
                enhanced_update["api_published"] = details["publishedDateTime"]
                logger.debug(
                    f"Retrieved API publication date: {details['publishedDateTime']}"
                )

            # Update category information
            if "categories" in details and details["categories"]:
                enhanced_update["api_categories"] = details["categories"]
                logger.debug(f"Retrieved API categories: {details['categories']}")

        logger.info(
            f"Enhancement with detailed information completed: {update.get('title', 'Unknown')}"
        )
        return enhanced_update

    def __del__(self):
        """Resource cleanup"""
        if hasattr(self, "api_session"):
            self.api_session.close()

    def fetch_rss_feed(self) -> Optional[feedparser.FeedParserDict]:
        """
        Fetch RSS feed (try multiple URLs)

        Returns:
            Parsed feed (None on failure)
        """
        for url in self.RSS_URLS:
            try:
                logger.info("Fetching RSS feed")

                # Set up HTTP session for more robust feed retrieval
                session = requests.Session()
                retry_strategy = Retry(
                    total=2,
                    backoff_factor=1,
                    status_forcelist=[429, 500, 502, 503, 504],
                )
                adapter = HTTPAdapter(max_retries=retry_strategy)
                session.mount("http://", adapter)
                session.mount("https://", adapter)

                # Header configuration
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                    "Accept": "application/rss+xml, application/xml, text/xml, */*",
                    "Accept-Language": "en-US,en;q=0.9",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Connection": "keep-alive",
                    "Cache-Control": "no-cache",
                }

                # Retrieve feed via HTTP session
                feed = None
                try:
                    response = session.get(url, headers=headers, timeout=30)
                    response.raise_for_status()

                    # Log response content (for debugging)
                    logger.debug(f"HTTP status: {response.status_code}")
                    logger.debug(
                        f"Content-Type: {response.headers.get('Content-Type', 'Unknown')}"
                    )
                    logger.debug(f"Response length: {len(response.content)} bytes")

                    # Check if response is not empty
                    if not response.content:
                        logger.warning("RSS feed response is empty")
                        continue

                    # Detect and decode character encoding
                    content_bytes = response.content
                    logger.debug(f"First 100 bytes of response: {content_bytes[:100]}")

                    # First check encoding from Content-Type header
                    content_type = response.headers.get("Content-Type", "")
                    encoding = "utf-8"  # Default

                    if "charset=" in content_type:
                        try:
                            encoding = (
                                content_type.split("charset=")[1].split(";")[0].strip()
                            )
                            logger.debug(
                                f"Encoding detected from Content-Type: {encoding}"
                            )
                        except:
                            logger.debug(
                                "Failed to detect encoding from Content-Type, using UTF-8"
                            )

                    # Try multiple encodings (prioritize BOM support)
                    content_str = None
                    tried_encodings = [
                        "utf-8-sig",
                        encoding,
                        "utf-8",
                        "latin1",
                        "cp1252",
                    ]

                    for enc in tried_encodings:
                        try:
                            content_str = content_bytes.decode(enc)
                            logger.debug(f"Successfully decoded with encoding '{enc}'")
                            break
                        except UnicodeDecodeError as e:
                            logger.debug(f"Failed to decode with encoding '{enc}': {e}")
                            continue

                    if content_str is None:
                        # Last resort: decode ignoring errors
                        content_str = content_bytes.decode("utf-8", errors="replace")
                        logger.warning(
                            "All encodings failed, decoded with error replacement"
                        )

                    content_stripped = content_str.strip()

                    # Remove BOM (Byte Order Mark)
                    if content_stripped.startswith("\ufeff"):
                        content_stripped = content_stripped[1:]
                        logger.debug("Detected and removed UTF-8 BOM")

                    # Debug: examine content beginning in detail
                    logger.debug(
                        f"First 50 characters of response: '{content_stripped[:50]}'"
                    )
                    logger.debug(
                        f"Byte representation of response beginning: {content_stripped[:50].encode('unicode_escape')}"
                    )

                    # Check each condition individually and log output
                    starts_with_xml_header = content_stripped.startswith("<?xml")
                    starts_with_rss = content_stripped.startswith("<rss")
                    starts_with_feed = content_stripped.startswith("<feed")
                    starts_with_angle = content_stripped.startswith("<")

                    logger.debug(f"XML validity check results:")
                    logger.debug(
                        f"  - Starts with XML header ('<?xml'): {starts_with_xml_header}"
                    )
                    logger.debug(f"  - Starts with RSS tag ('<rss'): {starts_with_rss}")
                    logger.debug(
                        f"  - Starts with Feed tag ('<feed'): {starts_with_feed}"
                    )
                    logger.debug(f"  - Starts with any tag ('<'): {starts_with_angle}")

                    # Check if it looks like XML (more lenient)
                    is_xml_like = (
                        starts_with_xml_header
                        or starts_with_rss
                        or starts_with_feed
                        or starts_with_angle
                    )

                    logger.debug(f"Final determination is_xml_like: {is_xml_like}")

                    if not is_xml_like:
                        logger.warning("Response is not XML")
                        logger.warning(
                            f"First 200 characters of response: {content_str[:200]}"
                        )
                        logger.warning(
                            f"First bytes of response: {content_str[:50].encode('unicode_escape')}"
                        )
                        continue

                    logger.info(f"XML format confirmed OK: {content_stripped[:100]}...")

                    # Parse with feedparser
                    logger.debug("Starting feedparser parsing...")
                    feed = feedparser.parse(response.content)
                    logger.debug(
                        f"feedparser parsing completed: bozo={getattr(feed, 'bozo', 'Unknown')}"
                    )

                except requests.exceptions.RequestException as e:
                    logger.warning(f"HTTP request error: {type(e).__name__}")
                    # Fallback: try direct retrieval with feedparser
                    logger.info("Fallback: trying direct retrieval with feedparser")
                    feed = feedparser.parse(url)
                    logger.debug("Fallback feedparser parsing completed")

                finally:
                    session.close()

                # Check feed parsing results
                logger.debug(
                    f"Feed object verification: {type(feed)} - hasattr(feed, 'entries'): {hasattr(feed, 'entries')}"
                )

                if not feed:
                    logger.warning("Could not retrieve feed")
                    continue

                # First check existence of entries
                has_entries = hasattr(feed, "entries") and len(feed.entries) > 0
                logger.debug(
                    f"Entry verification: has_entries={has_entries}, entry count={len(feed.entries) if hasattr(feed, 'entries') else 'N/A'}"
                )

                if feed.bozo:
                    logger.debug(
                        f"Minor warning in feed parsing ({url}): {feed.bozo_exception}"
                    )

                    # Continue processing if entries exist despite warnings
                    if has_entries:
                        logger.info(
                            f"Parse warnings exist, but {len(feed.entries)} entries retrieved, continuing processing"
                        )
                    else:
                        logger.warning(
                            f"Could not retrieve entries due to parse error: {url}"
                        )
                        continue

                if not has_entries:
                    logger.warning("Feed has no entries")
                    continue

                logger.info(
                    f"Feed retrieval completed: {len(feed.entries)} entries ({url})"
                )

                # Log basic feed information
                if hasattr(feed, "feed"):
                    feed_info = feed.feed
                    logger.debug(f"Feed title: {feed_info.get('title', 'Unknown')}")
                    logger.debug(
                        f"Feed description: {feed_info.get('description', 'Unknown')}"
                    )
                    logger.debug(f"Last updated: {feed_info.get('updated', 'Unknown')}")

                return feed

            except Exception as e:
                logger.warning(f"Feed retrieval error: {type(e).__name__}")
                continue

        # If all URLs failed
        logger.error("Failed to retrieve feed from all RSS URLs")
        return None

    def parse_date(self, date_str: str) -> Optional[datetime]:
        """
        Parse date string (support multiple formats)

        Args:
            date_str: Date string

        Returns:
            datetime object (None on failure)
        """
        if not date_str:
            return None

        try:
            iso_date_str = date_str.strip()
            if iso_date_str.endswith("Z"):
                iso_date_str = iso_date_str[:-1] + "+00:00"

            parsed_dt = datetime.fromisoformat(iso_date_str)
            if parsed_dt.tzinfo is None:
                parsed_dt = parsed_dt.replace(tzinfo=timezone.utc)
            return parsed_dt
        except Exception as e:
            logger.debug(f"ISO8601 date parsing error: {date_str} - {e}")

        try:
            parsed_dt = parsedate_to_datetime(date_str)
            if parsed_dt and parsed_dt.tzinfo is None:
                parsed_dt = parsed_dt.replace(tzinfo=timezone.utc)
            return parsed_dt
        except Exception as e:
            logger.debug(f"RFC2822 date parsing error: {date_str} - {e}")

        # Fallback: try common date formats
        date_formats = [
            "%Y-%m-%dT%H:%M:%S.%fZ",
            "%Y-%m-%dT%H:%M:%SZ",
            "%Y-%m-%dT%H:%M:%S",
            "%Y-%m-%d %H:%M:%S",
            "%a, %d %b %Y %H:%M:%S %z",
            "%a, %d %b %Y %H:%M:%S GMT",
            "%Y-%m-%dT%H:%M:%S%z",
        ]

        for fmt in date_formats:
            try:
                # Treat as UTC if no timezone information
                if "%z" in fmt:
                    parsed_dt = datetime.strptime(date_str, fmt)
                else:
                    parsed_dt = datetime.strptime(date_str, fmt).replace(
                        tzinfo=timezone.utc
                    )
                return parsed_dt
            except ValueError:
                continue

        logger.debug(f"Failed to parse with all date formats: {date_str}")
        return None

    def filter_recent_updates(self, feed: feedparser.FeedParserDict) -> List[Dict]:
        """
        Filter updates within specified timeframe

        Args:
            feed: Parsed feed

        Returns:
            Filtered update list
        """
        recent_updates = []

        for entry in feed.entries:
            # Get publication date (prioritize a10:updated for Azure Updates)
            published_date = None

            # 1. First check a10:updated (actual update time for Azure Updates)
            if hasattr(entry, "updated"):
                published_date = self.parse_date(entry.updated)
                logger.debug(
                    f"Date retrieved from a10:updated: {entry.updated} -> {published_date}"
                )

            # 2. Fallback: check published
            if not published_date and hasattr(entry, "published"):
                published_date = self.parse_date(entry.published)
                logger.debug(
                    f"Date retrieved from published: {entry.published} -> {published_date}"
                )

            # 3. Last resort: check updated_parsed
            if (
                not published_date
                and hasattr(entry, "updated_parsed")
                and entry.updated_parsed
            ):
                try:
                    published_date = datetime(
                        *entry.updated_parsed[:6], tzinfo=timezone.utc
                    )
                    logger.debug(
                        f"Date retrieved from updated_parsed: {entry.updated_parsed} -> {published_date}"
                    )
                except Exception as e:
                    logger.debug(f"updated_parsed parsing error: {e}")

            if not published_date:
                logger.debug(
                    f"Skipping entry without retrievable date: {entry.get('title', 'Unknown')}"
                )
                continue

            # Check if within specified timeframe
            if published_date >= self.cutoff_time:
                update_info = {
                    "title": entry.get("title", ""),
                    "description": entry.get("description", ""),
                    "link": entry.get("link", ""),
                    "published": published_date,
                    "categories": [
                        tag.get("term", "") for tag in entry.get("tags", [])
                    ],
                }

                # Retrieve detailed information in details mode
                if self.details_mode:
                    update_info = self.enhance_update_with_details(update_info)

                recent_updates.append(update_info)
                logger.info(f"Found target update: {update_info['title']}")

        logger.info(f"Found {len(recent_updates)} recent updates")
        return recent_updates

    def group_updates_by_date(self, updates: List[Dict]) -> Dict[str, List[Dict]]:
        """
        Group updates by publication date (UTC)

        Args:
            updates: Update list

        Returns:
            Dictionary with date string as key and update list as value
        """
        from collections import defaultdict

        grouped = defaultdict(list)
        for update in updates:
            pub_date = update.get("published")
            if pub_date:
                date_key = pub_date.strftime("%Y-%m-%d")
                grouped[date_key].append(update)
            else:
                logger.warning(
                    f"Skipping update without publication date: {update.get('title', 'Unknown')}"
                )

        # Sort by date
        sorted_grouped = dict(sorted(grouped.items()))
        logger.info(f"Grouped {len(updates)} updates into {len(sorted_grouped)} days")
        for date_key, items in sorted_grouped.items():
            logger.info(f"  {date_key}: {len(items)} items")

        return sorted_grouped

    def process_updates(self) -> List[Dict]:
        """
        Process updates and generate summaries

        Returns:
            Update list with summaries
        """
        # Retrieve RSS feed
        feed = self.fetch_rss_feed()
        if not feed:
            return []

        # Filter recent updates
        recent_updates = self.filter_recent_updates(feed)
        if not recent_updates:
            logger.info("No new updates within specified timeframe")
            return []

        # Summarize each update
        processed_updates = []
        for i, update in enumerate(recent_updates, 1):
            logger.info(
                f"Processing update ({i}/{len(recent_updates)}): {update['title']}"
            )

            # Consider API rate limits and wait briefly
            if i > 1:
                time.sleep(1)

            # Generate summary (use API detailed information in details mode)
            api_details = (
                update if self.details_mode and update.get("api_details") else None
            )
            summary = self.openai_client.summarize_update(
                update["title"], update["description"], update["link"], api_details
            )

            update["summary"] = summary

            # Generate detailed summary in details mode
            if self.details_mode:
                # Additional wait for API rate limiting
                time.sleep(1)

                # Determine content for detailed summary (prioritize API information)
                detail_title = update.get("api_title", update["title"])
                detail_content = update.get("api_content", update["description"])

                detailed_summary = self.openai_client.generate_detailed_summary(
                    detail_title, detail_content, update["link"]
                )
                update["detailed_summary"] = detailed_summary

                if detailed_summary:
                    logger.info(
                        f"Detailed summary generation completed: {update['title'][:50]}..."
                    )
                else:
                    logger.warning(
                        f"Detailed summary generation failed: {update['title'][:50]}..."
                    )

            processed_updates.append(update)

            if summary:
                mode_info = "Details mode" if self.details_mode else "Standard mode"
                logger.info(
                    f"Summary generation completed ({mode_info}): {update['title'][:50]}..."
                )
            else:
                logger.warning(f"Summary generation failed: {update['title'][:50]}...")

        return processed_updates

    def process_backfill(
        self,
        output_dir: str = "updates_en",
        force: bool = False,
        backfill_days: Optional[int] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
    ) -> Dict[str, str]:
        """
        Backfill mode: Retrieve updates for specified period and generate reports per date

        When both backfill_days and start_date are specified, start_date takes priority.

        Args:
            output_dir: Output directory
            force: Whether to overwrite existing files
            backfill_days: Number of days to go back (used when start_date is not specified)
            start_date: Backfill start date (from this date onwards)
            end_date: Backfill end date (up to this date, defaults to today)

        Returns:
            Dictionary of date -> file path
        """
        # Determine end date
        today_date = datetime.now(timezone.utc).date()
        if end_date:
            backfill_end = (
                end_date.date() if isinstance(end_date, datetime) else end_date
            )
        else:
            backfill_end = today_date

        # Determine start date
        if start_date:
            backfill_start = (
                start_date.date() if isinstance(start_date, datetime) else start_date
            )
            backfill_days_calc = (backfill_end - backfill_start).days + 1
            logger.info(
                f"Backfill mode started: {backfill_start} - {backfill_end} ({backfill_days_calc} days)"
            )
        elif backfill_days:
            backfill_days_calc = backfill_days
            backfill_start = backfill_end - timedelta(days=backfill_days - 1)
            logger.info(
                f"Backfill mode started: {backfill_start} - {backfill_end} (past {backfill_days} days)"
            )
        else:
            logger.error("Either backfill_days or start_date must be specified")
            return {}

        if backfill_days_calc <= 0:
            logger.error(
                f"End date ({backfill_end}) is before start date ({backfill_start})"
            )
            return {}

        # Reset cutoff time for backfill target
        original_cutoff = self.cutoff_time
        self.cutoff_time = datetime(
            backfill_start.year,
            backfill_start.month,
            backfill_start.day,
            tzinfo=timezone.utc,
        )
        logger.info(f"Backfill cutoff time: {self.cutoff_time}")

        # Retrieve RSS feed
        feed = self.fetch_rss_feed()
        if not feed:
            self.cutoff_time = original_cutoff
            return {}

        # Filter updates for entire period
        all_updates = self.filter_recent_updates(feed)
        if not all_updates:
            logger.info("No updates found for backfill period")
            self.cutoff_time = original_cutoff
            return {}

        # Group by date
        grouped = self.group_updates_by_date(all_updates)

        # Create date list for generation target (all dates within backfill period)
        all_dates = []
        for i in range(backfill_days_calc):
            target_date = backfill_start + timedelta(days=i)
            all_dates.append(target_date.strftime("%Y-%m-%d"))
        all_dates.sort()

        saved_files = {}
        total_dates = len(all_dates)

        for idx, date_str in enumerate(all_dates, 1):
            # Check output file path
            filepath = os.path.join(output_dir, f"azure-updates-{date_str}.md")

            # Check for existing file
            if os.path.exists(filepath) and not force:
                logger.info(f"Skipping (file exists, no --force): {filepath}")
                continue

            updates_for_date = grouped.get(date_str, [])
            logger.info(
                f"Backfill processing ({idx}/{total_dates}): {date_str} - {len(updates_for_date)} items"
            )

            # Summarize each update
            processed = []
            for i, update in enumerate(updates_for_date, 1):
                logger.info(
                    f"  [{date_str}] Processing update ({i}/{len(updates_for_date)}): {update['title'][:50]}..."
                )

                # Wait for API rate limiting
                if len(processed) > 0:
                    time.sleep(1)

                # Generate summary
                api_details = (
                    update if self.details_mode and update.get("api_details") else None
                )
                summary = self.openai_client.summarize_update(
                    update["title"],
                    update["description"],
                    update["link"],
                    api_details,
                )
                update["summary"] = summary

                # Details mode
                if self.details_mode:
                    time.sleep(1)
                    detail_title = update.get("api_title", update["title"])
                    detail_content = update.get("api_content", update["description"])
                    detailed_summary = self.openai_client.generate_detailed_summary(
                        detail_title, detail_content, update["link"]
                    )
                    update["detailed_summary"] = detailed_summary

                processed.append(update)

            # Generate report (specify target date)
            target_date = datetime.strptime(date_str, "%Y-%m-%d")
            report_content = self.generate_markdown_report(
                processed, target_date=target_date
            )

            # Save
            output_path = self.save_report(
                report_content, output_dir, target_date=target_date
            )
            saved_files[date_str] = output_path
            logger.info(f"Backfill report saved: {output_path}")

        # Restore original cutoff time
        self.cutoff_time = original_cutoff

        logger.info(
            f"Backfill completed: Generated reports for {len(saved_files)} days"
        )
        return saved_files

    def generate_markdown_report(
        self, updates: List[Dict], target_date: Optional[datetime] = None
    ) -> str:
        """
        Generate markdown report

        Args:
            updates: Processed update list
            target_date: Report target date (defaults to today if not specified)

        Returns:
            Markdown format report
        """
        if target_date:
            today = target_date.strftime("%B %d, %Y")
        else:
            today = datetime.now().strftime("%B %d, %Y")
        mode_text = "Details Mode" if self.details_mode else "Standard Mode"
        report_lines = [
            f"# {today} - Azure Updates Summary Report ({mode_text})",
            f"",
            f"**Generated on**: {today}",
            f"**Target period**: Within the last {self.check_hours} hours",
            f"**Processing mode**: {mode_text}",
            f"**Number of updates**: {len(updates)} items",
            f"",
        ]

        if not updates:
            report_lines.extend(
                [
                    "## Results",
                    "",
                    "No updates found for today.",
                    "",
                ]
            )
        else:
            report_lines.extend(["## Update List", ""])

            for i, update in enumerate(updates, 1):
                # Determine display title (prioritize API information in details mode)
                display_title = update["title"]
                if self.details_mode and update.get("api_title"):
                    display_title = update["api_title"]

                report_lines.extend(
                    [
                        f"### {i}. {display_title}",
                        "",
                        f"**Published**: {update['published'].strftime('%B %d, %Y %H:%M:%S UTC')}",
                        f"**Link**: [{display_title}]({update['link']})",
                        "",
                    ]
                )

                # Display details mode information
                if self.details_mode and update.get("update_id"):
                    report_lines.extend(
                        [
                            f"**Update ID**: {update['update_id']}",
                            f"**Data source**: Azure Updates API",
                            "",
                        ]
                    )

                # Category information (prioritize API information in details mode)
                categories = update["categories"]
                if self.details_mode and update.get("api_categories"):
                    categories = update["api_categories"]

                if categories:
                    categories_str = (
                        ", ".join(categories)
                        if isinstance(categories, list)
                        else str(categories)
                    )
                    report_lines.extend([f"**Categories**: {categories_str}", ""])

                if update.get("summary"):
                    report_lines.extend(["**Summary**:", "", update["summary"], ""])
                else:
                    report_lines.extend(["**Summary**: Generation failed", ""])

                # Detailed content (Details mode: GPT detailed summary, Standard mode: API/RSS information)
                if self.details_mode and update.get("detailed_summary"):
                    # Details mode: Use GPT-generated detailed summary
                    report_lines.extend(
                        ["**Details**:", "", update["detailed_summary"], "", "---", ""]
                    )
                else:
                    # Standard mode: Use API information or RSS information
                    detail_content = update["description"]
                    if self.details_mode and update.get("api_content"):
                        detail_content = update["api_content"]
                    report_lines.extend(
                        ["**Details**:", "", detail_content, "", "---", ""]
                    )

        report_lines.extend(
            [
                "",
                f"*This report was automatically generated - {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}*",
            ]
        )

        return "\n".join(report_lines)

    def save_report(
        self,
        content: str,
        output_dir: str = "updates_en",
        target_date: Optional[datetime] = None,
    ) -> str:
        """
        Save report to file

        Args:
            content: Report content
            output_dir: Output directory
            target_date: Report target date (defaults to today if not specified)

        Returns:
            Saved file path
        """
        # Create output directory
        os.makedirs(output_dir, exist_ok=True)

        # Generate filename (target date or today's date)
        if target_date:
            date_str = target_date.strftime("%Y-%m-%d")
        else:
            date_str = datetime.now().strftime("%Y-%m-%d")
        filename = f"azure-updates-{date_str}.md"
        filepath = os.path.join(output_dir, filename)

        # Save file
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            logger.info(f"Report saved: {filepath}")
            return filepath
        except Exception as e:
            logger.error(f"File save error: {e}")
            raise


def load_config() -> Dict[str, str]:
    """
    Load configuration from environment variables (for DefaultAzureCredential authentication)

    Authentication method is automatically selected based on environment variable settings:
    - AZURE_TENANT_ID + AZURE_CLIENT_ID + AZURE_CLIENT_SECRET: Service principal authentication
    - AZURE_TENANT_ID + AZURE_CLIENT_ID + OIDC context: OIDC/Workload Identity authentication
    - AZURE_TENANT_ID + AZURE_CLIENT_ID only: Managed ID authentication
    - None of the above: Azure CLI credentials (for local development)

    Returns:
        Configuration dictionary
    """
    config = {
        "endpoint": os.getenv("AOAI_ENDPOINT"),
        "deployment": os.getenv("DEPLOYMENT"),
        "api_version": os.getenv("API_VER", "2025-01-01-preview"),
        "check_hours": int(os.getenv("CHECK_HOURS", "24")),
    }

    # Validate required settings (authentication is auto-determined by DefaultAzureCredential)
    required_vars = ["endpoint", "deployment"]
    missing_vars = [var for var in required_vars if not config[var]]

    if missing_vars:
        env_var_names = {
            "endpoint": "AOAI_ENDPOINT",
            "deployment": "DEPLOYMENT",
        }
        missing_env = [env_var_names.get(var, var.upper()) for var in missing_vars]
        logger.error(
            f"Required environment variables not set: {', '.join(missing_env)}"
        )
        sys.exit(1)

    # Log authentication method determination
    tenant_id = os.getenv("AZURE_TENANT_ID")
    client_id = os.getenv("AZURE_CLIENT_ID")
    client_secret = os.getenv("AZURE_CLIENT_SECRET")
    has_workload_identity_context = bool(
        os.getenv("AZURE_FEDERATED_TOKEN_FILE")
        or (
            os.getenv("ACTIONS_ID_TOKEN_REQUEST_URL")
            and os.getenv("ACTIONS_ID_TOKEN_REQUEST_TOKEN")
        )
    )

    if tenant_id and client_id and has_workload_identity_context:
        logger.info(
            "Configuration loaded (OIDC/Workload Identity authentication will be used)"
        )
    elif tenant_id and client_id and client_secret:
        logger.info(
            "Configuration loaded (service principal authentication will be used)"
        )
    elif tenant_id and client_id:
        logger.info("Configuration loaded (managed ID authentication will be used)")
    else:
        logger.info("Configuration loaded (Azure CLI credentials will be used)")

    return config


def main():
    """Main processing"""
    parser = argparse.ArgumentParser(
        description="Azure Updates RSS feed processing (DefaultAzureCredential authentication version)"
    )
    parser.add_argument(
        "--hours",
        type=int,
        help="Target check period in hours. Overrides CHECK_HOURS environment variable",
    )
    parser.add_argument(
        "--output-dir",
        default="updates_en",
        help="Output directory (default: updates_en)",
    )
    parser.add_argument("--verbose", action="store_true", help="Output detailed logs")
    parser.add_argument(
        "--test-feed", action="store_true", help="Only execute RSS feed test retrieval"
    )
    parser.add_argument(
        "--details",
        action="store_true",
        help="Details mode: Retrieve detailed information from Azure Updates API",
    )
    parser.add_argument(
        "--backfill-days",
        type=int,
        metavar="N",
        help="Backfill mode: Regenerate reports for the past N days per date",
    )
    parser.add_argument(
        "--backfill-startdate",
        type=str,
        metavar="YYYY-MM-DD",
        help="Backfill mode: Regenerate reports from the specified date onwards",
    )
    parser.add_argument(
        "--backfill-enddate",
        type=str,
        metavar="YYYY-MM-DD",
        help="Backfill mode: Generate reports up to the specified date (default: today)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing files during backfill (default: skip)",
    )

    args = parser.parse_args()

    # Set log level
    if args.verbose:
        logger.setLevel(logging.DEBUG)

    try:
        # Test mode
        if args.test_feed:
            logger.info("Running in RSS feed test mode...")
            processor = AzureUpdatesProcessor(
                None, 24, False
            )  # No OpenAI client, details mode disabled
            feed = processor.fetch_rss_feed()
            if feed:
                print(f"\n✅ Feed retrieval successful!")
                print(f"📊 Entry count: {len(feed.entries)} items")

                # Display feed information
                if hasattr(feed, "feed"):
                    feed_info = feed.feed
                    print(f"📰 Feed title: {feed_info.get('title', 'Unknown')}")
                    print(
                        f"📝 Feed description: {feed_info.get('description', 'Unknown')[:100]}..."
                    )

                if len(feed.entries) > 0:
                    print(f"\n📋 Latest entry examples (max 5):")
                    for i, entry in enumerate(feed.entries[:5], 1):
                        title = entry.get("title", "No Title")
                        # Prioritize updated for Azure Updates
                        updated = entry.get(
                            "updated", entry.get("published", "No Date")
                        )
                        link = entry.get("link", "No Link")

                        print(f"  {i}. {title[:80]}...")
                        print(f"     📅 Updated: {updated}")
                        print(f"     🔗 Link: {link}")

                        # Update ID extraction test
                        update_id = processor.extract_update_id(link)
                        if update_id:
                            print(f"     🆔 Update ID: {update_id}")
                        else:
                            print(f"     ❌ Update ID extraction failed")

                        # Date parsing test
                        parsed_date = processor.parse_date(updated)
                        if parsed_date:
                            print(f"     ✅ Date parsing successful: {parsed_date}")
                        else:
                            print(f"     ❌ Date parsing failed")
                        print()

                print(
                    f"🎉 Test completed: RSS feed can be retrieved and parsed normally"
                )
            else:
                print("\n❌ Feed retrieval failed")
                print("Check log file azure_updates.log")
            return

        # Load configuration
        config = load_config()

        # Override time with command line argument
        if args.hours:
            config["check_hours"] = args.hours

        has_workload_identity_context = bool(
            os.getenv("AZURE_FEDERATED_TOKEN_FILE")
            or (
                os.getenv("ACTIONS_ID_TOKEN_REQUEST_URL")
                and os.getenv("ACTIONS_ID_TOKEN_REQUEST_TOKEN")
            )
        )
        if has_workload_identity_context and "AZURE_CLIENT_SECRET" in os.environ:
            logger.warning(
                "OIDC/Workload Identity context detected; ignoring AZURE_CLIENT_SECRET"
            )
            os.environ.pop("AZURE_CLIENT_SECRET", None)

        # Create DefaultAzureCredential
        # Authentication method is automatically selected based on environment variables:
        #   - AZURE_TENANT_ID + AZURE_CLIENT_ID + AZURE_CLIENT_SECRET -> Service principal authentication
        #   - AZURE_TENANT_ID + AZURE_CLIENT_ID + OIDC context
        #       (ACTIONS_ID_TOKEN_REQUEST_URL/TOKEN or AZURE_FEDERATED_TOKEN_FILE) -> OIDC/Workload Identity authentication
        #   - AZURE_TENANT_ID + AZURE_CLIENT_ID only -> Managed ID authentication
        #   - Not set -> Azure CLI credentials (for local development)
        credential = DefaultAzureCredential(
            exclude_environment_credential=has_workload_identity_context
        )

        # Initialize Azure OpenAI client (DefaultAzureCredential authentication)
        openai_client = AzureOpenAIClient(
            endpoint=config["endpoint"],
            credential=credential,
            deployment=config["deployment"],
            api_version=config["api_version"],
        )

        # Initialize Azure Updates processor
        processor = AzureUpdatesProcessor(
            openai_client=openai_client,
            check_hours=config["check_hours"],
            details_mode=args.details,
        )

        # Backfill mode
        backfill_start = None
        backfill_end = None
        if args.backfill_startdate:
            try:
                backfill_start = datetime.strptime(
                    args.backfill_startdate, "%Y-%m-%d"
                ).replace(tzinfo=timezone.utc)
            except ValueError:
                logger.error(
                    f"Invalid start date format: {args.backfill_startdate} (please use YYYY-MM-DD format)"
                )
                sys.exit(1)
        if args.backfill_enddate:
            try:
                backfill_end = datetime.strptime(
                    args.backfill_enddate, "%Y-%m-%d"
                ).replace(tzinfo=timezone.utc)
            except ValueError:
                logger.error(
                    f"Invalid end date format: {args.backfill_enddate} (please use YYYY-MM-DD format)"
                )
                sys.exit(1)

        if args.backfill_days or backfill_start:
            if backfill_start and backfill_end:
                logger.info(
                    f"Backfill mode: Regenerating {args.backfill_startdate} - {args.backfill_enddate}"
                )
            elif backfill_start:
                logger.info(
                    f"Backfill mode: Regenerating from {args.backfill_startdate} onwards"
                )
            else:
                logger.info(
                    f"Backfill mode: Regenerating past {args.backfill_days} days"
                )
            saved_files = processor.process_backfill(
                output_dir=args.output_dir,
                force=args.force,
                backfill_days=args.backfill_days,
                start_date=backfill_start,
                end_date=backfill_end,
            )

            # Display results
            mode_info = "Details mode" if args.details else "Standard mode"
            print(f"\n✅ Backfill completed! ({mode_info})")
            print(f"📊 Generated files: {len(saved_files)} days")

            if saved_files:
                print(f"\n📋 Generated file list:")
                for date_str in sorted(saved_files.keys()):
                    print(f"  📁 {date_str}: {saved_files[date_str]}")

            logger.info("Backfill processing completed successfully")
        else:
            # Normal mode
            # Process updates
            logger.info("Starting Azure Updates processing")
            updates = processor.process_updates()

            # Generate report
            logger.info("Generating markdown report")
            report_content = processor.generate_markdown_report(updates)

            # Save report
            output_path = processor.save_report(report_content, args.output_dir)

            # Display results
            mode_info = "Details mode" if args.details else "Standard mode"
            print(f"\n✅ Processing completed! ({mode_info})")
            print(f"📊 Processed items: {len(updates)} items")
            print(f"📁 Output file: {output_path}")

            if len(updates) > 0:
                print(f"\n📋 Update list:")
                for i, update in enumerate(updates, 1):
                    status = "✅" if update.get("summary") else "❌"
                    api_indicator = (
                        "🔍" if args.details and update.get("update_id") else ""
                    )
                    print(f"  {i}. {status}{api_indicator} {update['title'][:60]}...")

            logger.info("Processing completed successfully")

    except KeyboardInterrupt:
        logger.info("Processing interrupted by user")
        sys.exit(130)
    except Exception as e:
        logger.error(f"Unexpected error occurred: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
