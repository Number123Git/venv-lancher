# ライブラリのインポート
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




root.mainloop()