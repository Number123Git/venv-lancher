# ライブラリのインポート
import os

def path_check(output_dir):
    if os.path.isdir(output_dir):
        return True  # 出力先フォルダが存在する場合はTrueを返す
    else:
        return False  # 出力先フォルダが存在しない場合はFalseを返す