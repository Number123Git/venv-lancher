# ライブラリのインポート
from tkinter import ttk
from tkinter import BooleanVar
from tkinter import filedialog
from tkinter import messagebox
from ttkthemes import ThemedTk
import subprocess
from utils.path_utils import path_check


# 出力先フォルダの選択
def dirdialog_clicked():
    output_dir_path = filedialog.askdirectory(title="環境構築先フォルダを選択")
    # 出力先フォルダが選択された場合、エントリにパスを設定
    if output_dir_path:
        output_dir_entry.delete(0, "end")
        output_dir_entry.insert(0, output_dir_path)


# 実行ボタンが押された時の処理
def run_button_clicked():
    output_dir = output_dir_entry.get()  # 環境構築先フォルダのパスを取得
    env_name = env_name_entry.get()  # 環境名を取得
    package_command = package_entry.get()  # インストールするパッケージを取得
    requirements = requirements_var.get()  # 依存関係を記録するかどうかを取得

    path_check(output_dir)  # 出力先フォルダの存在チェック

# ttkthemeによるテーマの設定
root = ThemedTk()

# ウィンドウのタイトルとサイズを設定
root.title("venv-Lancher")
window_width = 800
window_height = 600

# ウィンドウを中央に配置
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width - window_width) / 2)
y = int((screen_height - window_height) / 2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")


# 出力先フォルダの選択
output_label = ttk.Label(root, text="環境構築するフォルダを選択", font=("Yu Gothic UI", 11))
output_dir_entry = ttk.Entry(root, width=50, font=("Yu Gothic UI", 11))
# 参照ボタンの作成
output_button = ttk.Button(root, text="参照", command=dirdialog_clicked)


# 環境名の入力
env_name_label = ttk.Label(root, text="環境名を入力", font=("Yu Gothic UI", 11))
env_name_entry = ttk.Entry(root, width=50, font=("Yu Gothic UI", 11))


# インストールするパッケージの入力
package_label = ttk.Label(root, text="インストールするパッケージのコマンドを入力", font=("Yu Gothic UI", 11))
package_entry = ttk.Entry(root, width=50, font=("Yu Gothic UI", 11))
package_info_label = ttk.Label(root, text="入力方式：pip install [パッケージ名]", font=("Yu Gothic UI", 10, "italic"))

# 空行用のダミーラベル
dummy_label_1 = ttk.Label(root, text="")


# 依存関係の記録の有無を確認
requirements_var = BooleanVar(value=False)  # 初期値をFalse（チェック状態）に設定
requirements_label = ttk.Label(root, text="依存関係を記録しますか？", font=("Yu Gothic UI", 11))
requirements_checkbutton = ttk.Checkbutton(root, text="記録する", variable=requirements_var)

# 空行用のダミーラベル
dummy_label_2 = ttk.Label(root, text="")

# 実行ボタン
run_button = ttk.Button(root, text="環境を構築", padding=[30,10], command = run_button_clicked)

# グリッドレイアウトの設定
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=0)
root.grid_columnconfigure(2, weight=0)
root.grid_columnconfigure(3, weight=0)
root.grid_columnconfigure(4, weight=1)

output_label.grid(row=0, column=1, columnspan=1, pady=10)
output_dir_entry.grid(row=0, column=2, columnspan=1, padx=5)
output_button.grid(row=0, column=3, columnspan=1, padx=5)

env_name_label.grid(row=1, column=1, columnspan=1, pady=10)
env_name_entry.grid(row=1, column=2, columnspan=1, padx=5)

package_label.grid(row=2, column=1, columnspan=1, pady=10)
package_entry.grid(row=2, column=2, columnspan=1, padx=5)
package_info_label.grid(row=3, column=1, columnspan=1, padx=5)

dummy_label_1.grid(row=4, column=1, columnspan=1, pady=10)

requirements_label.grid(row=5, column=1, columnspan=1, pady=10)
requirements_checkbutton.grid(row=5, column=2, columnspan=1, padx=5)

dummy_label_2.grid(row=6, column=1, columnspan=1, pady=10)

run_button.grid(row=7, column=1, columnspan=3, pady=20)

root.mainloop()