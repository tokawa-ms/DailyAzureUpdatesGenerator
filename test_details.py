#!/usr/bin/env python3
"""
Azure Updates 詳細モードのテストスクリプト

このスクリプトは以下をテストします：
1. RSSフィードからアップデートIDの抽出
2. Azure Updates APIからの詳細情報取得
3. 詳細情報を使った要約生成
"""

import os
import sys
import logging
from typing import Dict, Optional

# 相対インポート
from getlatestupdate import AzureUpdatesProcessor, AzureOpenAIClient

# ロギング設定
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("test_details.log", encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
logger = logging.getLogger(__name__)


def test_update_id_extraction():
    """アップデートID抽出のテスト"""
    print("\n🧪 テスト1: アップデートID抽出")
    print("=" * 50)

    processor = AzureUpdatesProcessor(None, 24, True)

    test_urls = [
        "https://azure.microsoft.com/updates?id=498568",
        "https://azure.microsoft.com/en-us/updates/?id=123456",
        "https://azure.microsoft.com/updates/some-feature/?id=789012",
        "https://azure.microsoft.com/updates/invalid-url",
        "https://example.com/some-other-site?id=999999",
    ]

    for url in test_urls:
        update_id = processor.extract_update_id(url)
        status = "✅" if update_id else "❌"
        print(f"{status} {url}")
        if update_id:
            print(f"    🆔 抽出されたID: {update_id}")
        else:
            print(f"    ❌ ID抽出失敗")
        print()


def test_api_details_fetch():
    """API詳細情報取得のテスト"""
    print("\n🧪 テスト2: API詳細情報取得")
    print("=" * 50)

    processor = AzureUpdatesProcessor(None, 24, True)

    # 実際のアップデートIDでテスト（これらは実在するかもしれないID）
    test_ids = [
        "498568",  # 例のID
        "999999",  # 存在しないID
        "123456",  # テスト用ID
    ]

    for update_id in test_ids:
        print(f"🔍 アップデートID {update_id} の詳細情報を取得中...")
        details = processor.fetch_update_details(update_id)

        if details:
            print(f"✅ 詳細情報取得成功")
            if isinstance(details, dict):
                print(f"    📋 取得されたフィールド: {list(details.keys())}")
                if "title" in details:
                    print(f"    📝 タイトル: {details['title'][:100]}...")
                if "content" in details and details["content"]:
                    print(f"    📄 本文長: {len(details['content'])} 文字")
            else:
                print(f"    📊 データ型: {type(details)}")
        else:
            print(f"❌ 詳細情報取得失敗")
        print()


def test_rss_with_details():
    """RSS + 詳細モードのテスト"""
    print("\n🧪 テスト3: RSS + 詳細モード統合テスト")
    print("=" * 50)

    processor = AzureUpdatesProcessor(None, 24, True)

    # RSSフィードを取得
    print("📡 RSSフィードを取得中...")
    feed = processor.fetch_rss_feed()

    if not feed:
        print("❌ RSSフィード取得失敗")
        return

    print(f"✅ RSSフィード取得成功: {len(feed.entries)} エントリ")

    # 最初の数件をテスト
    test_count = min(3, len(feed.entries))
    print(f"\n📋 最初の{test_count}件で詳細情報テスト:")

    for i, entry in enumerate(feed.entries[:test_count], 1):
        title = entry.get("title", "No Title")
        link = entry.get("link", "")

        print(f"\n{i}. {title[:80]}...")
        print(f"   🔗 リンク: {link}")

        # アップデートIDを抽出
        update_id = processor.extract_update_id(link)
        if update_id:
            print(f"   🆔 アップデートID: {update_id}")

            # 詳細情報を取得
            details = processor.fetch_update_details(update_id)
            if details:
                print(f"   ✅ 詳細情報取得成功")

                # 基本更新情報を作成
                update_info = {
                    "title": title,
                    "description": entry.get("description", ""),
                    "link": link,
                }

                # 詳細情報で拡張
                enhanced = processor.enhance_update_with_details(update_info)

                if enhanced.get("api_details"):
                    print(f"   🔍 拡張情報:")
                    if enhanced.get("api_title"):
                        print(f"      📝 APIタイトル: {enhanced['api_title'][:60]}...")
                    if enhanced.get("api_content"):
                        print(
                            f"      📄 API本文長: {len(enhanced['api_content'])} 文字"
                        )
                else:
                    print(f"   ❌ 拡張情報なし")
            else:
                print(f"   ❌ 詳細情報取得失敗")
        else:
            print(f"   ❌ アップデートID抽出失敗")


def test_with_openai():
    """OpenAI統合テスト（環境変数が設定されている場合）"""
    print("\n🧪 テスト4: OpenAI統合テスト")
    print("=" * 50)

    # 環境変数チェック
    required_vars = ["AOAI_ENDPOINT", "AOAI_KEY", "DEPLOYMENT"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]

    if missing_vars:
        print(f"❌ OpenAI環境変数が不足しているためスキップ: {', '.join(missing_vars)}")
        return

    try:
        # OpenAIクライアント初期化
        openai_client = AzureOpenAIClient(
            endpoint=os.getenv("AOAI_ENDPOINT"),
            api_key=os.getenv("AOAI_KEY"),
            deployment=os.getenv("DEPLOYMENT"),
            api_version=os.getenv("API_VER", "2025-01-01-preview"),
        )

        # プロセッサを詳細モードで初期化
        processor = AzureUpdatesProcessor(openai_client, 24, True)

        print("✅ OpenAIクライアント初期化成功")

        # サンプル更新情報を作成
        sample_update = {
            "title": "Azure Container Apps の新機能追加",
            "description": "Azure Container Apps に新しい機能が追加されました。この機能により、開発者はより効率的にコンテナアプリケーションを管理できるようになります。",
            "link": "https://azure.microsoft.com/updates?id=498568",
        }

        print("\n📝 サンプル更新情報で要約テスト:")
        print(f"タイトル: {sample_update['title']}")

        # 詳細情報で拡張
        enhanced_update = processor.enhance_update_with_details(sample_update)

        # 要約生成（詳細情報あり）
        api_details = enhanced_update if enhanced_update.get("api_details") else None
        summary = openai_client.summarize_update(
            enhanced_update["title"],
            enhanced_update["description"],
            enhanced_update["link"],
            api_details,
        )

        if summary:
            print("✅ 要約生成成功:")
            print(f"📄 要約: {summary}")
        else:
            print("❌ 要約生成失敗")

    except Exception as e:
        print(f"❌ OpenAI統合テストエラー: {e}")


def main():
    """メインテスト処理"""
    print("🧪 Azure Updates 詳細モード テストスイート")
    print("=" * 60)

    try:
        # テスト1: アップデートID抽出
        test_update_id_extraction()

        # テスト2: API詳細情報取得
        test_api_details_fetch()

        # テスト3: RSS + 詳細モード統合
        test_rss_with_details()

        # テスト4: OpenAI統合（環境変数が設定されている場合）
        test_with_openai()

        print("\n🎉 全テスト完了!")
        print("詳細ログは test_details.log で確認できます")

    except KeyboardInterrupt:
        print("\n⚠️ テストがユーザーによって中断されました")
    except Exception as e:
        print(f"\n❌ 予期しないエラー: {e}")
        logger.error(f"テスト実行エラー: {e}", exc_info=True)


if __name__ == "__main__":
    main()
