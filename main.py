# ライブラリのインポート
from tkinter import ttk
from ttkthemes import ThemedTk


# ttkthemeによるテーマの設定
root = ThemedTk(theme="breeze")

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
output_label = ttk.Label(root, text="環境構築するフォルダを選択", font=("Yu Gothic UI", 12))
output_folder = ttk.Entry(root, width=50, font=("Yu Gothic UI", 12))
output_button = ttk.Button(root, text="参照")

# グリッドレイアウトの設定
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=0)
root.grid_columnconfigure(2, weight=0)
root.grid_columnconfigure(3, weight=0)
root.grid_columnconfigure(4, weight=1)

output_label.grid(row=0, column=1, columnspan=1, pady=10)
output_folder.grid(row=0, column=2, columnspan=1, padx=5)
output_button.grid(row=0, column=3, columnspan=1, padx=5)

root.mainloop()