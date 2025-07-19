#!/usr/bin/env python3
"""
Azure Updates RSS フィードを読み込み、指定時間内の更新を Azure OpenAI で要約するアプリケーション

環境変数:
- AOAI_ENDPOINT: Azure OpenAI エンドポイント
- AOAI_KEY: Azure OpenAI API キー
- DEPLOYMENT: Azure OpenAI デプロイメント名
- API_VER: Azure OpenAI API バージョン
- CHECK_HOURS: チェック対象時間（デフォルト: 24時間）
"""

import os
import sys
import logging
import argparse
from datetime import datetime, timedelta, timezone
from typing import List, Dict, Optional
import json
import time

# サードパーティライブラリ
import feedparser
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

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
    """Azure OpenAI クライアント"""

    def __init__(self, endpoint: str, api_key: str, deployment: str, api_version: str):
        """
        Azure OpenAI クライアントを初期化

        Args:
            endpoint: Azure OpenAI エンドポイント
            api_key: API キー
            deployment: デプロイメント名
            api_version: API バージョン
        """
        self.endpoint = endpoint.rstrip("/")
        self.api_key = api_key
        self.deployment = deployment
        self.api_version = api_version

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

        # ヘッダー設定
        self.session.headers.update(
            {"Content-Type": "application/json", "api-key": self.api_key}
        )

        logger.info("Azure OpenAI クライアントを初期化しました")

    def summarize_update(
        self, title: str, description: str, link: str
    ) -> Optional[str]:
        """
        Azure Update を日本語で要約

        Args:
            title: アップデートのタイトル
            description: アップデートの詳細
            link: アップデートのリンク

        Returns:
            要約テキスト（失敗時はNone）
        """
        try:
            url = f"{self.endpoint}/openai/deployments/{self.deployment}/chat/completions?api-version={self.api_version}"

            # プロンプト作成
            prompt = f"""
以下のAzure Updateを日本語で簡潔に要約してください。技術者向けに重要なポイントを含めてください。

タイトル: {title}

詳細: {description}

リンク: {link}

要約は以下の形式で作成してください：
- 何が更新されたか
- 主な変更点や新機能
- 影響を受ける対象
- 注意点があれば記載

200文字程度で簡潔にまとめてください。
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

            response = self.session.post(url, json=payload, timeout=30)
            response.raise_for_status()

            result = response.json()

            if "choices" in result and len(result["choices"]) > 0:
                summary = result["choices"][0]["message"]["content"].strip()
                logger.info(f"要約完了: {title[:50]}...")
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

    def __init__(self, openai_client: AzureOpenAIClient, check_hours: int = 24):
        """
        プロセッサを初期化

        Args:
            openai_client: Azure OpenAI クライアント
            check_hours: チェック対象時間（時間）
        """
        self.openai_client = openai_client
        self.check_hours = check_hours
        self.cutoff_time = datetime.now(timezone.utc) - timedelta(hours=check_hours)

        logger.info(f"チェック対象時間: {check_hours}時間以内")
        logger.info(f"カットオフ時間: {self.cutoff_time}")

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
                recent_updates.append(update_info)
                logger.info(f"対象更新を発見: {update_info['title']}")

        logger.info(f"{len(recent_updates)}件の最新更新を発見")
        return recent_updates

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

            # 要約生成
            summary = self.openai_client.summarize_update(
                update["title"], update["description"], update["link"]
            )

            update["summary"] = summary
            processed_updates.append(update)

            if summary:
                logger.info(f"要約生成完了: {update['title'][:50]}...")
            else:
                logger.warning(f"要約生成失敗: {update['title'][:50]}...")

        return processed_updates

    def generate_markdown_report(self, updates: List[Dict]) -> str:
        """
        マークダウンレポートを生成

        Args:
            updates: 処理済み更新リスト

        Returns:
            マークダウン形式のレポート
        """
        today = datetime.now().strftime("%Y年%m月%d日")
        report_lines = [
            f"# {today} - Azure Updates 要約レポート",
            f"",
            f"**生成日時**: {today}",
            f"**対象期間**: 過去 {self.check_hours} 時間以内",
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
                report_lines.extend(
                    [
                        f"### {i}. {update['title']}",
                        "",
                        f"**公開日時**: {update['published'].strftime('%Y年%m月%d日 %H:%M:%S UTC')}",
                        f"**リンク**: [{update['title']}]({update['link']})",
                        "",
                    ]
                )

                if update["categories"]:
                    categories_str = ", ".join(update["categories"])
                    report_lines.extend([f"**カテゴリ**: {categories_str}", ""])

                if update.get("summary"):
                    report_lines.extend(["**要約**:", "", update["summary"], ""])
                else:
                    report_lines.extend(["**要約**: 生成に失敗しました", ""])

                report_lines.extend(
                    ["**詳細**:", "", update["description"], "", "---", ""]
                )

        report_lines.extend(
            [
                "",
                f"*このレポートは自動生成されました - {datetime.now(timezone(timedelta(hours=9))).strftime('%Y-%m-%d %H:%M:%S JST')}*",
            ]
        )

        return "\n".join(report_lines)

    def save_report(self, content: str, output_dir: str = "updates") -> str:
        """
        レポートをファイルに保存

        Args:
            content: レポート内容
            output_dir: 出力ディレクトリ

        Returns:
            保存されたファイルパス
        """
        # 出力ディレクトリを作成
        os.makedirs(output_dir, exist_ok=True)

        # ファイル名生成（本日の日付）
        today = datetime.now().strftime("%Y-%m-%d")
        filename = f"azure-updates-{today}.md"
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
    環境変数から設定を読み込み

    Returns:
        設定辞書
    """
    config = {
        "endpoint": os.getenv("AOAI_ENDPOINT"),
        "api_key": os.getenv("AOAI_KEY"),
        "deployment": os.getenv("DEPLOYMENT"),
        "api_version": os.getenv("API_VER", "2025-01-01-preview"),
        "check_hours": int(os.getenv("CHECK_HOURS", "24")),
    }

    # 必須設定の検証
    required_vars = ["endpoint", "api_key", "deployment"]
    missing_vars = [var for var in required_vars if not config[var]]

    if missing_vars:
        logger.error(
            f"必須環境変数が設定されていません: {', '.join([var.upper() for var in missing_vars])}"
        )
        sys.exit(1)

    logger.info("設定を読み込みました")
    return config


def main():
    """メイン処理"""
    parser = argparse.ArgumentParser(description="Azure Updates RSS フィード処理")
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

    args = parser.parse_args()

    # ログレベル設定
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    try:
        # テストモードの場合
        if args.test_feed:
            logger.info("RSSフィードテストモードで実行中...")
            processor = AzureUpdatesProcessor(None, 24)  # OpenAI クライアントなし
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

        # Azure OpenAI クライアント初期化
        openai_client = AzureOpenAIClient(
            endpoint=config["endpoint"],
            api_key=config["api_key"],
            deployment=config["deployment"],
            api_version=config["api_version"],
        )

        # Azure Updates プロセッサ初期化
        processor = AzureUpdatesProcessor(
            openai_client=openai_client, check_hours=config["check_hours"]
        )

        # 更新処理
        logger.info("Azure Updates の処理を開始します")
        updates = processor.process_updates()

        # レポート生成
        logger.info("マークダウンレポートを生成中")
        report_content = processor.generate_markdown_report(updates)

        # レポート保存
        output_path = processor.save_report(report_content, args.output_dir)

        # 結果表示
        print(f"\n✅ 処理完了!")
        print(f"📊 処理件数: {len(updates)} 件")
        print(f"📁 出力ファイル: {output_path}")

        if len(updates) > 0:
            print(f"\n📋 更新一覧:")
            for i, update in enumerate(updates, 1):
                status = "✅" if update.get("summary") else "❌"
                print(f"  {i}. {status} {update['title'][:60]}...")

        logger.info("処理が正常に完了しました")

    except KeyboardInterrupt:
        logger.info("処理がユーザーによって中断されました")
        sys.exit(130)
    except Exception as e:
        logger.error(f"予期しないエラーが発生しました: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
