# ライブラリのインポート
import os
from win11toast import toast

def path_check(output_dir):
    if os.path.isdir(output_dir):
        return True  # 出力先フォルダが存在する場合はTrueを返す
    else:
        toast("エラー", "入力された出力先フォルダが存在しません。")  # 出力先フォルダが存在しない場合は通知を表示
        return False  # 出力先フォルダが存在しない場合はFalseを返す