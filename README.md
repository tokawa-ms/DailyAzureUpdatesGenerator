# Azure Updates 自動要約

## 概要

Azure Updates の自動要約が [updates](./updates) ディレクトリに保存されています。
自動要約機能は、GitHub Actions によって毎日日本時間の正午に実行され、直近一日の Azure Updates の情報を収集したうえ、日本語の要約を生成します。

## 免責事項

自動要約レポートは、RSS フィードから取得した情報を元に生成されており、正確性や完全性を保証するものではありません。利用者は、提供された情報を自己責任で使用してください。
もし興味がある内容があれば、レポート中に含まれるリンクを参照して、元の情報を確認することをお勧めします。

# Azure Updates RSS フィード処理アプリケーション

このアプリケーションは、Azure Updates の RSS フィードを読み込み、指定した時間以内に更新があった Azure の Update 情報を Azure OpenAI の GPT-4.1-mini モデルで日本語に要約し、マークダウン形式でファイルに出力します。

## 機能

- **堅牢な RSS フィード取得**: 複数の URL を試行して確実にフィードを取得
- **詳細モード**: Azure Updates API から詳細情報を取得（`--details` オプション）
- 指定時間内の新しい更新のフィルタリング
- Azure OpenAI を使用した日本語要約生成
- マークダウン形式での詳細レポート出力
- 包括的なエラーハンドリングとリトライ機能
- 詳細なログ出力とモニタリング
- **テストモード**: フィード取得のテスト機能

## 必要な環境変数

アプリケーションを実行する前に、以下の環境変数を設定してください：

- `AOAI_ENDPOINT`: Azure OpenAI エンドポイント URL
- `AOAI_KEY`: Azure OpenAI API キー
- `DEPLOYMENT`: Azure OpenAI デプロイメント名
- `API_VER`: Azure OpenAI API バージョン（デフォルト: 2024-02-15-preview）
- `CHECK_HOURS`: チェック対象時間（時間単位、デフォルト: 24）

## インストール

1. 必要なパッケージをインストール：

```cmd
pip install -r requirements.txt
```

2. RSS フィードのテスト：

```cmd
test_feed.bat
```

または

```cmd
python getlatestupdate.py --test-feed --verbose
```

## 使用方法

### テスト実行（推奨：最初に実行）

```cmd
# RSS フィードのテスト取得
python getlatestupdate.py --test-feed --verbose

# バッチファイルでのテスト実行
test_feed.bat
```

### 基本的な使用方法

```cmd
python getlatestupdate.py
```

### オプション付きの実行

```cmd
# 過去12時間の更新をチェック
python getlatestupdate.py --hours 12

# 詳細モード（Azure Updates APIから詳細情報を取得）
python getlatestupdate.py --details

# 出力ディレクトリを指定
python getlatestupdate.py --output-dir reports

# 詳細ログを出力
python getlatestupdate.py --verbose

# RSSフィードのテストのみ実行
python getlatestupdate.py --test-feed

# 複数のオプションを組み合わせ（詳細モード + 詳細ログ + 72時間）
python getlatestupdate.py --details --verbose --hours 72
```

### 詳細モードの使用方法

詳細モード（`--details`）では、RSS フィードの情報に加えて Azure Updates API から詳細な情報を取得します：

```cmd
# 詳細モードで実行
python getlatestupdate.py --details

# 詳細モードを含む実行例バッチファイル
run_details_example.bat
```

**詳細モードの特徴：**

- Azure Updates API から各記事の詳細情報を取得
- より正確で完全な記事タイトルと本文を使用
- API から取得した情報をレポートに表示
- 詳細な情報源の追跡とログ出力

### 環境変数の設定例（Windows）

```cmd
set AOAI_ENDPOINT=https://your-openai-resource.openai.azure.com
set AOAI_KEY=your-api-key-here
set DEPLOYMENT=gpt-4-mini
set API_VER=2024-02-15-preview
set CHECK_HOURS=24
```

## トラブルシューティング

### RSS フィード取得エラー

1. **テストモードで確認**:

   ```cmd
   python getlatestupdate.py --test-feed --verbose
   ```

2. **ログファイルを確認**: `azure_updates.log`

3. **ネットワーク接続確認**: インターネット接続とプロキシ設定

4. **複数 URL 試行**: アプリケーションは自動で複数の RSS URL を試行します

### 詳細モード関連のトラブルシューティング

1. **詳細モードのテスト**:

   ```cmd
   python test_details.py
   ```

2. **API アクセスエラー**: Azure Updates API が一時的に利用できない場合、標準モードで処理を続行

3. **アップデート ID 抽出失敗**: 一部の記事で ID が抽出できない場合は RSS 情報を使用

### 一般的なエラーと対処法

- **"フィードにエントリがありません"**: RSS URL が変更された可能性があります
- **"not well-formed (invalid token)"**: XML パースエラー。別の URL を試行中です
- **HTTP 接続エラー**: ネットワーク設定やファイアウォールを確認してください

## 出力

アプリケーションは以下を生成します：

1. **マークダウンレポート**: `updates/azure-updates-YYYY-MM-DD.md`
2. **ログファイル**: `azure_updates.log`

## レポートの内容

### 標準モード

- 生成日時と対象期間
- 更新件数の概要
- 各更新の詳細：
  - タイトル（RSS フィードから）
  - 公開日時
  - リンク
  - カテゴリ
  - AI 生成の日本語要約
  - 元の詳細説明（RSS フィードから）

### 詳細モード（`--details`）

上記に加えて：

- **アップデート ID**: 個別記事の識別子
- **情報源**: Azure Updates API 使用の明示
- **強化されたタイトル**: API から取得したより正確なタイトル
- **詳細な本文**: API から取得した完全な記事内容
- **改善された要約**: より詳細で正確な情報に基づく要約

## エラーハンドリング

- **複数 RSS URL**: 主要 URL が失敗した場合の自動フォールバック
- **ネットワークエラー**: 自動リトライとタイムアウト設定
- **XML パースエラー**: 軽微なエラーは無視して処理継続
- **API レート制限**: 適切な待機時間の設定
- **詳細ログ**: トラブルシューティング用の包括的なログ

## セキュリティ考慮事項

- API キーは環境変数から取得
- HTTPS 通信の使用
- 適切なタイムアウト設定
- セッション管理とリソースクリーンアップ
- User-Agent の適切な設定

## 制限事項

- Azure OpenAI のレート制限に依存
- RSS フィードの可用性に依存
- 日付パースの精度はフィードの形式に依存
