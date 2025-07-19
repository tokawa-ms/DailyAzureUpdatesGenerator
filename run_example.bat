@echo off
REM Azure Updates RSS フィード処理アプリケーション実行例
REM 
REM 使用前に以下の環境変数を設定してください：
REM set AOAI_ENDPOINT=https://your-openai-resource.openai.azure.com
REM set AOAI_KEY=your-api-key-here
REM set DEPLOYMENT=gpt-4.1-mini
REM set API_VER=2025-01-01-preview

echo Azure Updates RSS フィード処理を開始します...
echo.

REM 環境変数の確認
if "%AOAI_ENDPOINT%"=="" (
    echo エラー: AOAI_ENDPOINT 環境変数が設定されていません
    goto :error
)

if "%AOAI_KEY%"=="" (
    echo エラー: AOAI_KEY 環境変数が設定されていません
    goto :error
)

if "%DEPLOYMENT%"=="" (
    echo エラー: DEPLOYMENT 環境変数が設定されていません
    goto :error
)

echo 設定確認完了
echo エンドポイント: %AOAI_ENDPOINT%
echo デプロイメント: %DEPLOYMENT%
echo.

REM アプリケーション実行
python getlatestupdate.py --verbose

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ✅ 処理が正常に完了しました
) else (
    echo.
    echo ❌ 処理中にエラーが発生しました（終了コード: %ERRORLEVEL%）
)

pause
goto :end

:error
echo.
echo 環境変数を設定してから再実行してください
pause

:end
