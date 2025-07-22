@echo off
REM Azure Updates 詳細モード実行例
REM このスクリプトは詳細モード（--details）でAzure Updatesを取得します

echo ========================================
echo Azure Updates 詳細モード実行例
echo ========================================
echo.

REM 環境変数チェック
if "%AOAI_ENDPOINT%"=="" (
    echo エラー: AOAI_ENDPOINT 環境変数が設定されていません
    echo 以下の環境変数を設定してください：
    echo - AOAI_ENDPOINT: Azure OpenAI エンドポイント
    echo - AOAI_KEY: Azure OpenAI API キー  
    echo - DEPLOYMENT: Azure OpenAI デプロイメント名
    pause
    exit /b 1
)

if "%AOAI_KEY%"=="" (
    echo エラー: AOAI_KEY 環境変数が設定されていません
    pause
    exit /b 1
)

if "%DEPLOYMENT%"=="" (
    echo エラー: DEPLOYMENT 環境変数が設定されていません
    pause
    exit /b 1
)

echo ✅ 環境変数設定確認完了
echo.

REM 詳細モードで実行
echo 🔍 詳細モードでAzure Updatesを実行中...
echo   - Azure Updates APIから詳細情報を取得します
echo   - より正確で詳細な情報を使用して要約を生成します
echo.

python getlatestupdate.py --details --verbose --hours 72

echo.
echo ========================================
echo 詳細モード実行完了
echo ========================================
echo.
echo 📁 生成されたファイル:
echo   - updates\azure-updates-YYYY-MM-DD.md
echo   - azure_updates.log
echo.
echo 💡 ヒント:
echo   - --details: 詳細モード（Azure Updates APIを使用）
echo   - --verbose: 詳細ログ出力
echo   - --hours 72: 過去72時間の更新を対象
echo.

pause
