REM 引数の取得
set output_path=%1
set env_name=%2
set package=%3
set requirements=%4


REM 出力先フォルダへ移動
cd /d %output_path%

REM 仮想環境の作成
python -m venv %env_name%

REM 仮想環境をアクティブ化
call %env_name%\Scripts\activate

REM パッケージのインストール
if %package% == "" (
    %package%
)

REM 依存関係の記録
if %requirements% = ="True" (
    pip freeze > requirements.txt
)
