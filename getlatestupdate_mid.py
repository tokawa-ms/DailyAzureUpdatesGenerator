#!/usr/bin/env python3
"""
Azure Updates RSS フィードを読み込み、指定時間内の更新を Azure OpenAI で要約するアプリケーション
（DefaultAzureCredential 認証版）

認証方式:
- ローカル環境: Azure CLI クレデンシャル（az login 済みであること）
- クラウド環境（AZURE_TENANT_ID + AZURE_CLIENT_ID + AZURE_CLIENT_SECRET 設定時）: サービスプリンシパル認証
- クラウド環境（AZURE_TENANT_ID + AZURE_CLIENT_ID のみ設定時）: マネージド ID 認証

環境変数:
- AOAI_ENDPOINT: Azure OpenAI エンドポイント
- DEPLOYMENT: Azure OpenAI デプロイメント名
- API_VER: Azure OpenAI API バージョン
- CHECK_HOURS: チェック対象時間（デフォルト: 24時間）
- AZURE_TENANT_ID: Azure AD テナント ID（オプション、クラウド環境用）
- AZURE_CLIENT_ID: クライアント ID（オプション、クラウド環境用）
- AZURE_CLIENT_SECRET: クライアントシークレット（オプション、サービスプリンシパル認証用）
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
from urllib.parse import urlparse, parse_qs

# サードパーティライブラリ
from dotenv import load_dotenv

load_dotenv()

import feedparser
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Azure Identity ライブラリ
from azure.identity import DefaultAzureCredential
from azure.core.credentials import TokenCredential

# ロギング設定
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("azure_updates.log", encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
logger = logging.getLogger(__name__)


class AzureOpenAIClient:
    """Azure OpenAI クライアント（DefaultAzureCredential 認証）"""

    # Azure OpenAI / Azure Cognitive Services 用のスコープ
    _COGNITIVE_SERVICES_SCOPE = "https://cognitiveservices.azure.com/.default"

    def __init__(
        self,
        endpoint: str,
        credential: TokenCredential,
        deployment: str,
        api_version: str,
    ):
        """
        Azure OpenAI クライアントを初期化（DefaultAzureCredential 認証）

        Args:
            endpoint: Azure OpenAI エンドポイント
            credential: Azure Identity の TokenCredential（DefaultAzureCredential 等）
            deployment: デプロイメント名
            api_version: API バージョン
        """
        self.endpoint = endpoint.rstrip("/")
        self.credential = credential
        self.deployment = deployment
        self.api_version = api_version

        # トークンキャッシュ
        self._cached_token = None

        # HTTPセッションの設定（リトライ機能付き）
        self.session = requests.Session()
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

        # Content-Type ヘッダーのみ設定（認証はリクエスト時にトークンを付与）
        self.session.headers.update({"Content-Type": "application/json"})

        logger.info(
            "Azure OpenAI クライアントを初期化しました（DefaultAzureCredential 認証）"
        )

    def _get_token(self) -> str:
        """
        Azure AD トークンを取得（キャッシュ＆自動更新）

        Returns:
            Bearer トークン文字列
        """
        # キャッシュされたトークンが有効であればそのまま返す
        if self._cached_token and self._cached_token.expires_on > time.time() + 300:
            return self._cached_token.token

        # 新しいトークンを取得
        logger.info("Azure AD トークンを取得中...")
        self._cached_token = self.credential.get_token(self._COGNITIVE_SERVICES_SCOPE)
        logger.info("Azure AD トークンを取得しました")
        return self._cached_token.token

    def _get_auth_headers(self) -> Dict[str, str]:
        """
        認証ヘッダーを生成

        Returns:
            Bearer トークンを含む認証ヘッダー辞書
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
        Azure Update を日本語で要約

        Args:
            title: アップデートのタイトル
            description: アップデートの詳細
            link: アップデートのリンク
            api_details: API から取得した詳細情報（オプション）

        Returns:
            要約テキスト（失敗時はNone）
        """
        try:
            url = f"{self.endpoint}/openai/deployments/{self.deployment}/chat/completions?api-version={self.api_version}"

            # 詳細モードの場合はAPI情報を使用
            content_source = "RSS"
            actual_title = title
            actual_content = description

            if api_details:
                content_source = "API"
                # APIから取得したタイトルがあれば使用
                if api_details.get("api_title"):
                    actual_title = api_details["api_title"]

                # APIから取得した本文があれば使用
                if api_details.get("api_content"):
                    actual_content = api_details["api_content"]

                logger.info(
                    f"要約処理で{content_source}情報を使用: {actual_title[:50]}..."
                )

            # プロンプト作成
            prompt = f"""
以下のAzure Updateを日本語で簡潔に要約してください。技術者向けに重要なポイントを含めてください。

タイトル: {actual_title}

詳細: {actual_content}

リンク: {link}

要約は以下の形式で作成してください：
- 何が更新されたか
- 主な変更点や新機能
- 影響を受ける対象
- 注意点があれば記載

1000文字程度で簡潔にまとめてください。
言葉遣いは「ですます調」に統一してください。
技術者が理解しやすいように、専門用語を適切に使用してください。
与えられた情報から要約を生成し、内容を補完するためのアップデート内容についての推測は行わないでください。

情報源: {content_source}データを使用
"""

            payload = {
                "messages": [
                    {
                        "role": "system",
                        "content": "あなたはAzureの専門家です。Azure Updateの内容を技術者向けに分かりやすく日本語で要約します。",
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
                logger.info(f"要約完了({content_source}): {actual_title[:50]}...")
                return summary
            else:
                logger.error("予期しないレスポンス形式を受信しました")
                return None

        except requests.exceptions.RequestException as e:
            logger.error("API リクエストエラーが発生しました")
            return None
        except Exception as e:
            logger.error("要約処理エラーが発生しました")
            return None

    def generate_detailed_summary(
        self, title: str, content: str, link: str
    ) -> Optional[str]:
        """
        詳細モード用の詳細要約を生成（500文字以内）

        Args:
            title: アップデートのタイトル
            content: アップデートの詳細内容
            link: アップデートのリンク

        Returns:
            詳細要約テキスト（失敗時はNone）
        """
        try:
            url = f"{self.endpoint}/openai/deployments/{self.deployment}/chat/completions?api-version={self.api_version}"

            # 詳細要約用のプロンプト作成
            prompt = f"""
以下のAzure Updateについて、技術者向けに詳細な説明を日本語で生成してください。
あなたは、レポートを生成する役割を与えられています。指示に対して人間が行うような返答は不要。淡々と詳細な要約文章を生成してください。

タイトル: {title}

詳細内容: {content}

リンク: {link}

以下の観点から詳細に説明してください：
- アップデートの背景と目的
- 具体的な機能や変更内容の詳細
- 技術的な仕組みや実装方法
- 活用シナリオや使用例
- 注意点や制限事項
- 関連するAzureサービスとの連携

500文字以内で、技術者が実際に活用する際に役立つ詳細情報を提供してください。
"""

            payload = {
                "messages": [
                    {
                        "role": "system",
                        "content": "あなたはAzureの専門家です。Azure Updateの詳細を技術者向けに分かりやすく日本語で解説します。実用的で具体的な情報を提供してください。",
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
                logger.info(f"詳細要約完了: {title[:50]}...")
                return detailed_summary
            else:
                logger.error("詳細要約で予期しないレスポンス形式を受信しました")
                return None

        except requests.exceptions.RequestException as e:
            logger.error("詳細要約のAPI リクエストエラーが発生しました")
            return None
        except Exception as e:
            logger.error("詳細要約処理エラーが発生しました")
            return None

    def __del__(self):
        """リソースクリーンアップ"""
        if hasattr(self, "session"):
            self.session.close()


class AzureUpdatesProcessor:
    """Azure Updates RSS フィード処理クラス"""

    # Azure Updates の複数のRSS URLを試行
    RSS_URLS = [
        "https://www.microsoft.com/releasecommunications/api/v2/azure/rss",
        "https://azurecomcdn.azureedge.net/en-us/updates/feed/",
        "https://azure.microsoft.com/en-us/updates/feed/",
    ]

    # Azure Updates API の基本URL
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
        プロセッサを初期化

        Args:
            openai_client: Azure OpenAI クライアント
            check_hours: チェック対象時間（時間）
            details_mode: 詳細モード（APIから詳細情報を取得）
        """
        self.openai_client = openai_client
        self.check_hours = check_hours
        self.details_mode = details_mode
        self.cutoff_time = datetime.now(timezone.utc) - timedelta(hours=check_hours)

        logger.info(f"チェック対象時間: {check_hours}時間以内")
        logger.info(f"カットオフ時間: {self.cutoff_time}")
        logger.info(f"詳細モード: {'有効' if details_mode else '無効'}")

        # APIアクセス用のHTTPセッションを初期化
        self.api_session = self._create_api_session()

    def _create_api_session(self) -> requests.Session:
        """
        Azure Updates API アクセス用のHTTPセッションを作成

        Returns:
            設定済みのHTTPセッション
        """
        session = requests.Session()

        # リトライ戦略
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("http://", adapter)
        session.mount("https://", adapter)

        # ブラウザを偽装するヘッダー設定
        session.headers.update(
            {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                "Accept": "application/json, text/plain, */*",
                "Accept-Language": "ja,en-US;q=0.9,en;q=0.8",
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

        logger.debug("Azure Updates API用HTTPセッションを初期化しました")
        return session

    def extract_update_id(self, link: str) -> Optional[str]:
        """
        Azure Updates のリンクからアップデートIDを抽出

        Args:
            link: Azure Updates のリンク

        Returns:
            アップデートID（抽出できない場合はNone）
        """
        try:
            # URLをパース
            parsed_url = urlparse(link)

            # クエリパラメータから id を取得
            query_params = parse_qs(parsed_url.query)
            if "id" in query_params and query_params["id"]:
                update_id = query_params["id"][0]
                logger.debug(f"アップデートID抽出成功: {update_id} from {link}")
                return update_id

            # フォールバック: URLパスから数字を抽出
            path_match = re.search(r"/(\d+)/?$", parsed_url.path)
            if path_match:
                update_id = path_match.group(1)
                logger.debug(f"パスからアップデートID抽出: {update_id} from {link}")
                return update_id

            logger.warning(f"アップデートIDを抽出できませんでした: {link}")
            return None

        except Exception as e:
            logger.error(f"アップデートID抽出エラー: {link} - {e}")
            return None

    def fetch_update_details(self, update_id: str) -> Optional[Dict]:
        """
        Azure Updates API から詳細情報を取得

        Args:
            update_id: アップデートID

        Returns:
            詳細情報辞書（取得失敗時はNone）
        """
        try:
            api_url = f"{self.AZURE_UPDATES_API_BASE}{update_id}"
            logger.info(f"API詳細情報取得中: {api_url}")

            response = self.api_session.get(api_url, timeout=30)
            response.raise_for_status()

            # レスポンスの詳細をログ出力
            logger.debug(f"API HTTP ステータス: {response.status_code}")
            logger.debug(
                f"API Content-Type: {response.headers.get('Content-Type', 'Unknown')}"
            )
            logger.debug(f"API レスポンス長: {len(response.content)} bytes")

            # JSONとして解析
            data = response.json()

            # データサイズ情報を計算
            json_str = json.dumps(data, ensure_ascii=False) if data else "{}"
            char_count = len(json_str)
            byte_count = len(json_str.encode("utf-8"))

            logger.info(
                f"API詳細情報取得成功: {update_id} ({char_count}文字, {byte_count}バイト)"
            )
            logger.debug(
                f"API レスポンス構造: {list(data.keys()) if isinstance(data, dict) else type(data)}"
            )

            return data

        except requests.exceptions.RequestException as e:
            logger.error(
                f"API詳細情報取得でHTTPエラー: {update_id} - {type(e).__name__}: {e}"
            )
            return None
        except json.JSONDecodeError as e:
            logger.error(f"API詳細情報のJSON解析エラー: {update_id} - {e}")
            return None
        except Exception as e:
            logger.error(f"API詳細情報取得で予期しないエラー: {update_id} - {e}")
            return None

    def enhance_update_with_details(self, update: Dict) -> Dict:
        """
        更新情報を詳細API情報で拡張

        Args:
            update: 基本更新情報

        Returns:
            拡張された更新情報
        """
        if not self.details_mode:
            return update

        # アップデートIDを抽出
        update_id = self.extract_update_id(update.get("link", ""))
        if not update_id:
            logger.warning(
                f"詳細情報取得をスキップ（IDなし）: {update.get('title', 'Unknown')}"
            )
            return update

        # API詳細情報を取得
        details = self.fetch_update_details(update_id)
        if not details:
            logger.warning(f"詳細情報取得失敗: {update.get('title', 'Unknown')}")
            return update

        # 詳細情報で更新を拡張
        enhanced_update = update.copy()
        enhanced_update["api_details"] = details
        enhanced_update["update_id"] = update_id

        # APIから取得した情報で既存情報を上書き/拡張
        if isinstance(details, dict):
            # タイトルの更新
            if "title" in details and details["title"]:
                enhanced_update["api_title"] = details["title"]
                logger.debug(f"APIタイトル取得: {details['title']}")

            # 本文の更新
            if "content" in details and details["content"]:
                enhanced_update["api_content"] = details["content"]
                logger.debug(f"API本文取得: {len(details['content'])} 文字")

            # 公開日の更新
            if "publishedDateTime" in details and details["publishedDateTime"]:
                enhanced_update["api_published"] = details["publishedDateTime"]
                logger.debug(f"API公開日取得: {details['publishedDateTime']}")

            # カテゴリ情報の更新
            if "categories" in details and details["categories"]:
                enhanced_update["api_categories"] = details["categories"]
                logger.debug(f"APIカテゴリ取得: {details['categories']}")

        logger.info(f"詳細情報で拡張完了: {update.get('title', 'Unknown')}")
        return enhanced_update

    def __del__(self):
        """リソースクリーンアップ"""
        if hasattr(self, "api_session"):
            self.api_session.close()

    def fetch_rss_feed(self) -> Optional[feedparser.FeedParserDict]:
        """
        RSS フィードを取得（複数URLを試行）

        Returns:
            パースされたフィード（失敗時はNone）
        """
        for url in self.RSS_URLS:
            try:
                logger.info("RSSフィードを取得中")

                # HTTPセッションを設定してより堅牢にフィードを取得
                session = requests.Session()
                retry_strategy = Retry(
                    total=2,
                    backoff_factor=1,
                    status_forcelist=[429, 500, 502, 503, 504],
                )
                adapter = HTTPAdapter(max_retries=retry_strategy)
                session.mount("http://", adapter)
                session.mount("https://", adapter)

                # ヘッダー設定
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                    "Accept": "application/rss+xml, application/xml, text/xml, */*",
                    "Accept-Language": "ja,en-US;q=0.9,en;q=0.8",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Connection": "keep-alive",
                    "Cache-Control": "no-cache",
                }

                # フィードをHTTPセッション経由で取得
                feed = None
                try:
                    response = session.get(url, headers=headers, timeout=30)
                    response.raise_for_status()

                    # レスポンスの内容をログ出力（デバッグ用）
                    logger.debug(f"HTTP ステータス: {response.status_code}")
                    logger.debug(
                        f"Content-Type: {response.headers.get('Content-Type', 'Unknown')}"
                    )
                    logger.debug(f"レスポンス長: {len(response.content)} bytes")

                    # レスポンスが空でないかチェック
                    if not response.content:
                        logger.warning("RSSフィードのレスポンスが空です")
                        continue

                    # 文字エンコーディングを検出・デコード
                    content_bytes = response.content
                    logger.debug(f"レスポンス最初の100バイト: {content_bytes[:100]}")

                    # まずContent-Typeヘッダーからエンコーディングを確認
                    content_type = response.headers.get("Content-Type", "")
                    encoding = "utf-8"  # デフォルト

                    if "charset=" in content_type:
                        try:
                            encoding = (
                                content_type.split("charset=")[1].split(";")[0].strip()
                            )
                            logger.debug(
                                f"Content-Typeから検出されたエンコーディング: {encoding}"
                            )
                        except:
                            logger.debug(
                                "Content-Typeからエンコーディング検出失敗、UTF-8を使用"
                            )

                    # 複数のエンコーディングを試行（BOM対応を優先）
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
                            logger.debug(f"エンコーディング '{enc}' でデコード成功")
                            break
                        except UnicodeDecodeError as e:
                            logger.debug(
                                f"エンコーディング '{enc}' でデコード失敗: {e}"
                            )
                            continue

                    if content_str is None:
                        # 最後の手段：エラーを無視してデコード
                        content_str = content_bytes.decode("utf-8", errors="replace")
                        logger.warning(
                            "すべてのエンコーディングが失敗、エラー無視でデコードしました"
                        )

                    content_stripped = content_str.strip()

                    # BOM（Byte Order Mark）を除去
                    if content_stripped.startswith("\ufeff"):
                        content_stripped = content_stripped[1:]
                        logger.debug("UTF-8 BOM を検出・除去しました")

                    # デバッグ用：コンテンツの先頭を詳しく確認
                    logger.debug(f"レスポンス先頭50文字: '{content_stripped[:50]}'")
                    logger.debug(
                        f"レスポンス先頭のバイト表現: {content_stripped[:50].encode('unicode_escape')}"
                    )

                    # 各条件を個別にチェックしてログ出力
                    starts_with_xml_header = content_stripped.startswith("<?xml")
                    starts_with_rss = content_stripped.startswith("<rss")
                    starts_with_feed = content_stripped.startswith("<feed")
                    starts_with_angle = content_stripped.startswith("<")

                    logger.debug(f"XML妥当性チェック結果:")
                    logger.debug(
                        f"  - XMLヘッダー ('<?xml') で開始: {starts_with_xml_header}"
                    )
                    logger.debug(f"  - RSSタグ ('<rss') で開始: {starts_with_rss}")
                    logger.debug(f"  - Feedタグ ('<feed') で開始: {starts_with_feed}")
                    logger.debug(f"  - 任意のタグ ('<') で開始: {starts_with_angle}")

                    # XMLとして妥当そうかチェック（より寛容に）
                    is_xml_like = (
                        starts_with_xml_header
                        or starts_with_rss
                        or starts_with_feed
                        or starts_with_angle
                    )

                    logger.debug(f"最終判定 is_xml_like: {is_xml_like}")

                    if not is_xml_like:
                        logger.warning("XMLではないレスポンス")
                        logger.warning(f"レスポンス先頭200文字: {content_str[:200]}")
                        logger.warning(
                            f"レスポンス先頭のバイト: {content_str[:50].encode('unicode_escape')}"
                        )
                        continue

                    logger.info(f"XMLフォーマット確認OK: {content_stripped[:100]}...")

                    # feedparser でパース
                    logger.debug("feedparser によるパース開始...")
                    feed = feedparser.parse(response.content)
                    logger.debug(
                        f"feedparser パース完了: bozo={getattr(feed, 'bozo', 'Unknown')}"
                    )

                except requests.exceptions.RequestException as e:
                    logger.warning(f"HTTP リクエストエラー: {type(e).__name__}")
                    # フォールバック: feedparser の直接取得を試行
                    logger.info("フォールバック: feedparser での直接取得を試行")
                    feed = feedparser.parse(url)
                    logger.debug("フォールバック feedparser パース完了")

                finally:
                    session.close()

                # フィードパース結果をチェック
                logger.debug(
                    f"フィードオブジェクト確認: {type(feed)} - hasattr(feed, 'entries'): {hasattr(feed, 'entries')}"
                )

                if not feed:
                    logger.warning("フィードが取得できませんでした")
                    continue

                # エントリの存在をまず確認
                has_entries = hasattr(feed, "entries") and len(feed.entries) > 0
                logger.debug(
                    f"エントリ確認: has_entries={has_entries}, エントリ数={len(feed.entries) if hasattr(feed, 'entries') else 'N/A'}"
                )

                if feed.bozo:
                    logger.debug(
                        f"フィードパースで軽微な警告 ({url}): {feed.bozo_exception}"
                    )

                    # エントリがあれば警告があっても処理続行
                    if has_entries:
                        logger.info(
                            f"パース警告がありますが、{len(feed.entries)}件のエントリが取得できたため処理を続行します"
                        )
                    else:
                        logger.warning(
                            f"パースエラーでエントリが取得できませんでした: {url}"
                        )
                        continue

                if not has_entries:
                    logger.warning("フィードにエントリがありません")
                    continue

                logger.info(
                    f"フィードを取得完了: {len(feed.entries)}件のエントリ ({url})"
                )

                # フィードの基本情報をログ出力
                if hasattr(feed, "feed"):
                    feed_info = feed.feed
                    logger.debug(
                        f"フィードタイトル: {feed_info.get('title', 'Unknown')}"
                    )
                    logger.debug(
                        f"フィード説明: {feed_info.get('description', 'Unknown')}"
                    )
                    logger.debug(f"最終更新: {feed_info.get('updated', 'Unknown')}")

                return feed

            except Exception as e:
                logger.warning(f"フィード取得エラー: {type(e).__name__}")
                continue

        # すべてのURLで失敗した場合
        logger.error("すべてのRSS URLでフィード取得に失敗しました")
        return None

    def parse_date(self, date_str: str) -> Optional[datetime]:
        """
        日付文字列をパース（複数フォーマット対応）

        Args:
            date_str: 日付文字列

        Returns:
            datetime オブジェクト（失敗時はNone）
        """
        if not date_str:
            return None

        try:
            # まず feedparser の標準パーサーを試行
            time_struct = feedparser._parse_date(date_str)
            if time_struct:
                return datetime(*time_struct[:6], tzinfo=timezone.utc)
        except Exception as e:
            logger.debug(f"feedparser による日付パースエラー: {date_str} - {e}")

        # フォールバック: 一般的な日付フォーマットを試行
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
                # タイムゾーン情報がない場合はUTCとして扱う
                if "%z" in fmt:
                    parsed_dt = datetime.strptime(date_str, fmt)
                else:
                    parsed_dt = datetime.strptime(date_str, fmt).replace(
                        tzinfo=timezone.utc
                    )
                return parsed_dt
            except ValueError:
                continue

        logger.debug(f"すべての日付フォーマットで解析に失敗: {date_str}")
        return None

    def filter_recent_updates(self, feed: feedparser.FeedParserDict) -> List[Dict]:
        """
        指定時間内の更新をフィルタリング

        Args:
            feed: パースされたフィード

        Returns:
            フィルタリングされた更新リスト
        """
        recent_updates = []

        for entry in feed.entries:
            # 公開日時を取得（Azure Updates では a10:updated を優先）
            published_date = None

            # 1. まず a10:updated を確認（Azure Updates の実際の更新日時）
            if hasattr(entry, "updated"):
                published_date = self.parse_date(entry.updated)
                logger.debug(
                    f"a10:updated から日付取得: {entry.updated} -> {published_date}"
                )

            # 2. フォールバック: published を確認
            if not published_date and hasattr(entry, "published"):
                published_date = self.parse_date(entry.published)
                logger.debug(
                    f"published から日付取得: {entry.published} -> {published_date}"
                )

            # 3. 最後の手段: updated_parsed を確認
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
                        f"updated_parsed から日付取得: {entry.updated_parsed} -> {published_date}"
                    )
                except Exception as e:
                    logger.debug(f"updated_parsed パースエラー: {e}")

            if not published_date:
                logger.debug(
                    f"日付が取得できないエントリをスキップ: {entry.get('title', 'Unknown')}"
                )
                continue

            # 指定時間内かチェック
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

                # 詳細モードの場合は詳細情報を取得
                if self.details_mode:
                    update_info = self.enhance_update_with_details(update_info)

                recent_updates.append(update_info)
                logger.info(f"対象更新を発見: {update_info['title']}")

        logger.info(f"{len(recent_updates)}件の最新更新を発見")
        return recent_updates

    def group_updates_by_date(self, updates: List[Dict]) -> Dict[str, List[Dict]]:
        """
        更新情報を公開日（UTC）でグルーピング

        Args:
            updates: 更新リスト

        Returns:
            日付文字列をキー、更新リストを値とする辞書
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
                    f"公開日が取得できない更新をスキップ: {update.get('title', 'Unknown')}"
                )

        # 日付でソート
        sorted_grouped = dict(sorted(grouped.items()))
        logger.info(
            f"{len(updates)}件の更新を{len(sorted_grouped)}日分にグルーピングしました"
        )
        for date_key, items in sorted_grouped.items():
            logger.info(f"  {date_key}: {len(items)}件")

        return sorted_grouped

    def process_updates(self) -> List[Dict]:
        """
        更新を処理して要約を生成

        Returns:
            要約付き更新リスト
        """
        # RSS フィード取得
        feed = self.fetch_rss_feed()
        if not feed:
            return []

        # 最新更新をフィルタリング
        recent_updates = self.filter_recent_updates(feed)
        if not recent_updates:
            logger.info("指定時間内に新しい更新はありません")
            return []

        # 各更新を要約
        processed_updates = []
        for i, update in enumerate(recent_updates, 1):
            logger.info(f"更新を処理中 ({i}/{len(recent_updates)}): {update['title']}")

            # APIレート制限を考慮して少し待機
            if i > 1:
                time.sleep(1)

            # 要約生成（詳細モードの場合はAPI詳細情報を使用）
            api_details = (
                update if self.details_mode and update.get("api_details") else None
            )
            summary = self.openai_client.summarize_update(
                update["title"], update["description"], update["link"], api_details
            )

            update["summary"] = summary

            # 詳細モードの場合は詳細要約も生成
            if self.details_mode:
                # APIレート制限を考慮して追加待機
                time.sleep(1)

                # 詳細要約用のコンテンツを決定（API情報を優先）
                detail_title = update.get("api_title", update["title"])
                detail_content = update.get("api_content", update["description"])

                detailed_summary = self.openai_client.generate_detailed_summary(
                    detail_title, detail_content, update["link"]
                )
                update["detailed_summary"] = detailed_summary

                if detailed_summary:
                    logger.info(f"詳細要約生成完了: {update['title'][:50]}...")
                else:
                    logger.warning(f"詳細要約生成失敗: {update['title'][:50]}...")

            processed_updates.append(update)

            if summary:
                mode_info = "詳細モード" if self.details_mode else "標準モード"
                logger.info(f"要約生成完了({mode_info}): {update['title'][:50]}...")
            else:
                logger.warning(f"要約生成失敗: {update['title'][:50]}...")

        return processed_updates

    def process_backfill(
        self,
        output_dir: str = "updates",
        force: bool = False,
        backfill_days: Optional[int] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
    ) -> Dict[str, str]:
        """
        バックフィルモード: 指定期間の更新を取得し、日付ごとにレポートを生成

        backfill_days と start_date の両方が指定された場合は start_date を優先。

        Args:
            output_dir: 出力ディレクトリ
            force: 既存ファイルを上書きするかどうか
            backfill_days: 遡る日数（start_date 未指定時に使用）
            start_date: バックフィル開始日（この日以降）
            end_date: バックフィル終了日（この日以前、省略時は本日）

        Returns:
            日付 -> ファイルパスの辞書
        """
        # 終了日を決定
        today_date = datetime.now(timezone.utc).date()
        if end_date:
            backfill_end = (
                end_date.date() if isinstance(end_date, datetime) else end_date
            )
        else:
            backfill_end = today_date

        # 開始日を決定
        if start_date:
            backfill_start = (
                start_date.date() if isinstance(start_date, datetime) else start_date
            )
            backfill_days_calc = (backfill_end - backfill_start).days + 1
            logger.info(
                f"バックフィルモード開始: {backfill_start} 〜 {backfill_end}（{backfill_days_calc}日分）"
            )
        elif backfill_days:
            backfill_days_calc = backfill_days
            backfill_start = backfill_end - timedelta(days=backfill_days - 1)
            logger.info(
                f"バックフィルモード開始: {backfill_start} 〜 {backfill_end}（過去{backfill_days}日分）"
            )
        else:
            logger.error("backfill_days または start_date のいずれかを指定してください")
            return {}

        if backfill_days_calc <= 0:
            logger.error(f"終了日({backfill_end})が開始日({backfill_start})より前です")
            return {}

        # カットオフ時間をバックフィル対象に合わせて再設定
        original_cutoff = self.cutoff_time
        self.cutoff_time = datetime(
            backfill_start.year,
            backfill_start.month,
            backfill_start.day,
            tzinfo=timezone.utc,
        )
        logger.info(f"バックフィルカットオフ時間: {self.cutoff_time}")

        # RSS フィード取得
        feed = self.fetch_rss_feed()
        if not feed:
            self.cutoff_time = original_cutoff
            return {}

        # 全期間分の更新をフィルタリング
        all_updates = self.filter_recent_updates(feed)
        if not all_updates:
            logger.info("バックフィル対象の更新はありません")
            self.cutoff_time = original_cutoff
            return {}

        # 日付ごとにグルーピング
        grouped = self.group_updates_by_date(all_updates)

        # 生成対象の日付リストを作成（バックフィル期間内の全日付）
        all_dates = []
        for i in range(backfill_days_calc):
            target_date = backfill_start + timedelta(days=i)
            all_dates.append(target_date.strftime("%Y-%m-%d"))
        all_dates.sort()

        saved_files = {}
        total_dates = len(all_dates)

        for idx, date_str in enumerate(all_dates, 1):
            # 出力先ファイルパスを確認
            filepath = os.path.join(output_dir, f"azure-updates-{date_str}.md")

            # 既存ファイルチェック
            if os.path.exists(filepath) and not force:
                logger.info(f"スキップ（ファイル既存、--force なし）: {filepath}")
                continue

            updates_for_date = grouped.get(date_str, [])
            logger.info(
                f"バックフィル処理中 ({idx}/{total_dates}): {date_str} - {len(updates_for_date)}件"
            )

            # 各更新を要約
            processed = []
            for i, update in enumerate(updates_for_date, 1):
                logger.info(
                    f"  [{date_str}] 更新を処理中 ({i}/{len(updates_for_date)}): {update['title'][:50]}..."
                )

                # APIレート制限を考慮して待機
                if len(processed) > 0:
                    time.sleep(1)

                # 要約生成
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

                # 詳細モード
                if self.details_mode:
                    time.sleep(1)
                    detail_title = update.get("api_title", update["title"])
                    detail_content = update.get("api_content", update["description"])
                    detailed_summary = self.openai_client.generate_detailed_summary(
                        detail_title, detail_content, update["link"]
                    )
                    update["detailed_summary"] = detailed_summary

                processed.append(update)

            # レポート生成（対象日付を指定）
            target_date = datetime.strptime(date_str, "%Y-%m-%d")
            report_content = self.generate_markdown_report(
                processed, target_date=target_date
            )

            # 保存
            output_path = self.save_report(
                report_content, output_dir, target_date=target_date
            )
            saved_files[date_str] = output_path
            logger.info(f"バックフィルレポート保存完了: {output_path}")

        # カットオフ時間を元に戻す
        self.cutoff_time = original_cutoff

        logger.info(f"バックフィル完了: {len(saved_files)}日分のレポートを生成しました")
        return saved_files

    def generate_markdown_report(
        self, updates: List[Dict], target_date: Optional[datetime] = None
    ) -> str:
        """
        マークダウンレポートを生成

        Args:
            updates: 処理済み更新リスト
            target_date: レポート対象日（指定がなければ本日）

        Returns:
            マークダウン形式のレポート
        """
        if target_date:
            today = target_date.strftime("%Y年%m月%d日")
        else:
            today = datetime.now().strftime("%Y年%m月%d日")
        mode_text = "詳細モード" if self.details_mode else "標準モード"
        report_lines = [
            f"# {today} - Azure Updates 要約レポート ({mode_text})",
            f"",
            f"**生成日時**: {today}",
            f"**対象期間**: 過去 {self.check_hours} 時間以内",
            f"**処理モード**: {mode_text}",
            f"**更新件数**: {len(updates)} 件",
            f"",
        ]

        if not updates:
            report_lines.extend(
                [
                    "## 結果",
                    "",
                    "本日の更新はありません。",
                    "",
                ]
            )
        else:
            report_lines.extend(["## 更新一覧", ""])

            for i, update in enumerate(updates, 1):
                # 表示用のタイトルを決定（詳細モードではAPI情報を優先）
                display_title = update["title"]
                if self.details_mode and update.get("api_title"):
                    display_title = update["api_title"]

                report_lines.extend(
                    [
                        f"### {i}. {display_title}",
                        "",
                        f"**公開日時**: {update['published'].strftime('%Y年%m月%d日 %H:%M:%S UTC')}",
                        f"**リンク**: [{display_title}]({update['link']})",
                        "",
                    ]
                )

                # 詳細モード情報の表示
                if self.details_mode and update.get("update_id"):
                    report_lines.extend(
                        [
                            f"**アップデートID**: {update['update_id']}",
                            f"**情報源**: Azure Updates API",
                            "",
                        ]
                    )

                # カテゴリ情報（詳細モードではAPI情報を優先）
                categories = update["categories"]
                if self.details_mode and update.get("api_categories"):
                    categories = update["api_categories"]

                if categories:
                    categories_str = (
                        ", ".join(categories)
                        if isinstance(categories, list)
                        else str(categories)
                    )
                    report_lines.extend([f"**カテゴリ**: {categories_str}", ""])

                if update.get("summary"):
                    report_lines.extend(["**要約**:", "", update["summary"], ""])
                else:
                    report_lines.extend(["**要約**: 生成に失敗しました", ""])

                # 詳細内容（詳細モードではGPT詳細要約、標準モードではAPI/RSS情報）
                if self.details_mode and update.get("detailed_summary"):
                    # 詳細モード：GPT生成の詳細要約を使用
                    report_lines.extend(
                        ["**詳細**:", "", update["detailed_summary"], "", "---", ""]
                    )
                else:
                    # 標準モード：API情報またはRSS情報を使用
                    detail_content = update["description"]
                    if self.details_mode and update.get("api_content"):
                        detail_content = update["api_content"]
                    report_lines.extend(
                        ["**詳細**:", "", detail_content, "", "---", ""]
                    )

        report_lines.extend(
            [
                "",
                f"*このレポートは自動生成されました - {datetime.now(timezone(timedelta(hours=9))).strftime('%Y-%m-%d %H:%M:%S JST')}*",
            ]
        )

        return "\n".join(report_lines)

    def save_report(
        self,
        content: str,
        output_dir: str = "updates",
        target_date: Optional[datetime] = None,
    ) -> str:
        """
        レポートをファイルに保存

        Args:
            content: レポート内容
            output_dir: 出力ディレクトリ
            target_date: レポート対象日（指定がなければ本日）

        Returns:
            保存されたファイルパス
        """
        # 出力ディレクトリを作成
        os.makedirs(output_dir, exist_ok=True)

        # ファイル名生成（対象日付または本日の日付）
        if target_date:
            date_str = target_date.strftime("%Y-%m-%d")
        else:
            date_str = datetime.now().strftime("%Y-%m-%d")
        filename = f"azure-updates-{date_str}.md"
        filepath = os.path.join(output_dir, filename)

        # ファイル保存
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            logger.info(f"レポートを保存しました: {filepath}")
            return filepath
        except Exception as e:
            logger.error(f"ファイル保存エラー: {e}")
            raise


def load_config() -> Dict[str, str]:
    """
    環境変数から設定を読み込み（DefaultAzureCredential 認証用）

    認証方式は環境変数の設定状況に応じて自動選択されます:
    - AZURE_TENANT_ID + AZURE_CLIENT_ID + AZURE_CLIENT_SECRET: サービスプリンシパル認証
    - AZURE_TENANT_ID + AZURE_CLIENT_ID のみ: マネージド ID 認証
    - 上記いずれも未設定: Azure CLI クレデンシャル（ローカル開発用）

    Returns:
        設定辞書
    """
    config = {
        "endpoint": os.getenv("AOAI_ENDPOINT"),
        "deployment": os.getenv("DEPLOYMENT"),
        "api_version": os.getenv("API_VER", "2025-01-01-preview"),
        "check_hours": int(os.getenv("CHECK_HOURS", "24")),
    }

    # 必須設定の検証（認証関連は DefaultAzureCredential が自動判定するため不要）
    required_vars = ["endpoint", "deployment"]
    missing_vars = [var for var in required_vars if not config[var]]

    if missing_vars:
        env_var_names = {
            "endpoint": "AOAI_ENDPOINT",
            "deployment": "DEPLOYMENT",
        }
        missing_env = [env_var_names.get(var, var.upper()) for var in missing_vars]
        logger.error(f"必須環境変数が設定されていません: {', '.join(missing_env)}")
        sys.exit(1)

    # 認証方式の判定ログ
    tenant_id = os.getenv("AZURE_TENANT_ID")
    client_id = os.getenv("AZURE_CLIENT_ID")
    client_secret = os.getenv("AZURE_CLIENT_SECRET")

    if tenant_id and client_id and client_secret:
        logger.info("設定を読み込みました（サービスプリンシパル認証が使用されます）")
    elif tenant_id and client_id:
        logger.info("設定を読み込みました（マネージド ID 認証が使用されます）")
    else:
        logger.info("設定を読み込みました（Azure CLI クレデンシャルが使用されます）")

    return config


def main():
    """メイン処理"""
    parser = argparse.ArgumentParser(
        description="Azure Updates RSS フィード処理（DefaultAzureCredential 認証版）"
    )
    parser.add_argument(
        "--hours",
        type=int,
        help="チェック対象時間（時間）。環境変数 CHECK_HOURS より優先されます",
    )
    parser.add_argument(
        "--output-dir",
        default="updates",
        help="出力ディレクトリ（デフォルト: updates）",
    )
    parser.add_argument("--verbose", action="store_true", help="詳細ログを出力")
    parser.add_argument(
        "--test-feed", action="store_true", help="RSSフィードのテスト取得のみ実行"
    )
    parser.add_argument(
        "--details",
        action="store_true",
        help="詳細モード: Azure Updates APIから詳細情報を取得",
    )
    parser.add_argument(
        "--backfill-days",
        type=int,
        metavar="N",
        help="バックフィルモード: 過去N日分のレポートを日付ごとに再生成",
    )
    parser.add_argument(
        "--backfill-startdate",
        type=str,
        metavar="YYYY-MM-DD",
        help="バックフィルモード: 指定日以降のレポートを日付ごとに再生成",
    )
    parser.add_argument(
        "--backfill-enddate",
        type=str,
        metavar="YYYY-MM-DD",
        help="バックフィルモード: 指定日までのレポートを生成（デフォルト: 本日）",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="バックフィル時に既存ファイルを上書き（デフォルトではスキップ）",
    )

    args = parser.parse_args()

    # ログレベル設定
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    try:
        # テストモードの場合
        if args.test_feed:
            logger.info("RSSフィードテストモードで実行中...")
            processor = AzureUpdatesProcessor(
                None, 24, False
            )  # OpenAI クライアントなし、詳細モード無効
            feed = processor.fetch_rss_feed()
            if feed:
                print(f"\n✅ フィード取得成功!")
                print(f"📊 エントリ数: {len(feed.entries)} 件")

                # フィード情報表示
                if hasattr(feed, "feed"):
                    feed_info = feed.feed
                    print(f"📰 フィードタイトル: {feed_info.get('title', 'Unknown')}")
                    print(
                        f"📝 フィード説明: {feed_info.get('description', 'Unknown')[:100]}..."
                    )

                if len(feed.entries) > 0:
                    print(f"\n📋 最新エントリ例（最大5件）:")
                    for i, entry in enumerate(feed.entries[:5], 1):
                        title = entry.get("title", "No Title")
                        # Azure Updates では updated を優先
                        updated = entry.get(
                            "updated", entry.get("published", "No Date")
                        )
                        link = entry.get("link", "No Link")

                        print(f"  {i}. {title[:80]}...")
                        print(f"     📅 更新日: {updated}")
                        print(f"     🔗 リンク: {link}")

                        # アップデートID抽出テスト
                        update_id = processor.extract_update_id(link)
                        if update_id:
                            print(f"     🆔 アップデートID: {update_id}")
                        else:
                            print(f"     ❌ アップデートID抽出失敗")

                        # 日付パーステスト
                        parsed_date = processor.parse_date(updated)
                        if parsed_date:
                            print(f"     ✅ 日付パース成功: {parsed_date}")
                        else:
                            print(f"     ❌ 日付パース失敗")
                        print()

                print(f"🎉 テスト完了: RSSフィードは正常に取得・パースできています")
            else:
                print("\n❌ フィード取得失敗")
                print("ログファイル azure_updates.log を確認してください")
            return

        # 設定読み込み
        config = load_config()

        # コマンドライン引数で時間を上書き
        if args.hours:
            config["check_hours"] = args.hours

        # DefaultAzureCredential を作成
        # 環境変数に応じて自動的に認証方式が選択される:
        #   - AZURE_TENANT_ID + AZURE_CLIENT_ID + AZURE_CLIENT_SECRET → サービスプリンシパル認証
        #   - AZURE_TENANT_ID + AZURE_CLIENT_ID のみ → マネージド ID 認証
        #   - 未設定 → Azure CLI クレデンシャル（ローカル開発用）
        credential = DefaultAzureCredential()

        # Azure OpenAI クライアント初期化（DefaultAzureCredential 認証）
        openai_client = AzureOpenAIClient(
            endpoint=config["endpoint"],
            credential=credential,
            deployment=config["deployment"],
            api_version=config["api_version"],
        )

        # Azure Updates プロセッサ初期化
        processor = AzureUpdatesProcessor(
            openai_client=openai_client,
            check_hours=config["check_hours"],
            details_mode=args.details,
        )

        # バックフィルモード
        backfill_start = None
        backfill_end = None
        if args.backfill_startdate:
            try:
                backfill_start = datetime.strptime(
                    args.backfill_startdate, "%Y-%m-%d"
                ).replace(tzinfo=timezone.utc)
            except ValueError:
                logger.error(
                    f"開始日の形式が不正です: {args.backfill_startdate}（YYYY-MM-DD 形式で指定してください）"
                )
                sys.exit(1)
        if args.backfill_enddate:
            try:
                backfill_end = datetime.strptime(
                    args.backfill_enddate, "%Y-%m-%d"
                ).replace(tzinfo=timezone.utc)
            except ValueError:
                logger.error(
                    f"終了日の形式が不正です: {args.backfill_enddate}（YYYY-MM-DD 形式で指定してください）"
                )
                sys.exit(1)

        if args.backfill_days or backfill_start:
            if backfill_start and backfill_end:
                logger.info(
                    f"バックフィルモード: {args.backfill_startdate} 〜 {args.backfill_enddate} を再生成します"
                )
            elif backfill_start:
                logger.info(
                    f"バックフィルモード: {args.backfill_startdate} 以降を再生成します"
                )
            else:
                logger.info(
                    f"バックフィルモード: 過去{args.backfill_days}日分を再生成します"
                )
            saved_files = processor.process_backfill(
                output_dir=args.output_dir,
                force=args.force,
                backfill_days=args.backfill_days,
                start_date=backfill_start,
                end_date=backfill_end,
            )

            # 結果表示
            mode_info = "詳細モード" if args.details else "標準モード"
            print(f"\n✅ バックフィル完了! ({mode_info})")
            print(f"📊 生成ファイル数: {len(saved_files)} 日分")

            if saved_files:
                print(f"\n📋 生成ファイル一覧:")
                for date_str in sorted(saved_files.keys()):
                    print(f"  📁 {date_str}: {saved_files[date_str]}")

            logger.info("バックフィル処理が正常に完了しました")
        else:
            # 通常モード
            # 更新処理
            logger.info("Azure Updates の処理を開始します")
            updates = processor.process_updates()

            # レポート生成
            logger.info("マークダウンレポートを生成中")
            report_content = processor.generate_markdown_report(updates)

            # レポート保存
            output_path = processor.save_report(report_content, args.output_dir)

            # 結果表示
            mode_info = "詳細モード" if args.details else "標準モード"
            print(f"\n✅ 処理完了! ({mode_info})")
            print(f"📊 処理件数: {len(updates)} 件")
            print(f"📁 出力ファイル: {output_path}")

            if len(updates) > 0:
                print(f"\n📋 更新一覧:")
                for i, update in enumerate(updates, 1):
                    status = "✅" if update.get("summary") else "❌"
                    api_indicator = (
                        "🔍" if args.details and update.get("update_id") else ""
                    )
                    print(f"  {i}. {status}{api_indicator} {update['title'][:60]}...")

            logger.info("処理が正常に完了しました")

    except KeyboardInterrupt:
        logger.info("処理がユーザーによって中断されました")
        sys.exit(130)
    except Exception as e:
        logger.error(f"予期しないエラーが発生しました: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
