@echo off
REM Azure Updates RSS フィードテスト実行スクリプト

echo Azure Updates RSS フィードのテストを開始します...
echo.

REM パッケージが正しくインストールされているかチェック
python -c "import feedparser; import requests; print('必要なパッケージが正常にインポートできました')" 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo エラー: 必要なパッケージがインストールされていません
    echo pip install -r requirements.txt を実行してください
    pause
    goto :end
)

echo 📦 必要なパッケージ確認完了
echo.

REM RSSフィードのテスト取得
echo 🔍 RSSフィードのテスト取得を実行中...
python getlatestupdate.py --test-feed --verbose

echo.
if %ERRORLEVEL% EQU 0 (
    echo ✅ RSSフィードテストが正常に完了しました
    echo.
    echo 次は実際の処理を実行してください：
    echo   1. 環境変数を設定
    echo   2. python getlatestupdate.py --verbose を実行
) else (
    echo ❌ RSSフィードテストでエラーが発生しました
    echo ログファイル azure_updates.log を確認してください
)

pause

:end
