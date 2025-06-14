import tkinter as tk
from tkinter import ttk
import subprocess
import tkinter.messagebox

def run_pytest():
    subprocess.run(["pytest", "-s", "appium_palapp_test.py"], cwd="c:/programs/GitHubWS/Appium/src")
    tk.messagebox.showinfo("完了", "テストが完了しました。")

def run_image_similarity():
    subprocess.run(["python", "image_similarity.py"], cwd="c:/programs/GitHubWS/Appium/src")
    tk.messagebox.showinfo("完了", "レポート作成が完了しました。")

root = tk.Tk()
root.title("Auto Tester")
root.geometry("800x420")
root.configure(bg="#222831")

# ttkテーマの設定（モダンな色合い）
style = ttk.Style()
style.theme_use("clam")
style.configure("TFrame", background="#222831")
style.configure("TLabel", background="#222831", foreground="#eeeeee")
style.configure("TButton", font=("Segoe UI", 12, "bold"), padding=8, background="#00adb5", foreground="#eeeeee")
style.map("TButton",
          background=[("active", "#393e46"), ("!active", "#00adb5")],
          foreground=[("active", "#00fff5"), ("!active", "#eeeeee")])
style.configure("TCheckbutton", background="#222831", foreground="#eeeeee", font=("Segoe UI", 10))
style.configure("TLabelframe", background="#222831", foreground="#00adb5", font=("Segoe UI", 12, "bold"))
style.configure("TLabelframe.Label", background="#222831", foreground="#00adb5", font=("Segoe UI", 12, "bold"))
style.configure("TCheckbutton", background="#222831", foreground="#ffd600", font=("Meiryo", 10))


title_label = ttk.Label(root, text="Auto Tester", font=("Segoe UI", 24, "bold"), foreground="#00adb5")
title_label.pack(pady=(24, 12))

main_frame = ttk.Frame(root)
main_frame.pack(pady=10, fill="both", expand=True)

# 左側：ボタンを縦並び
button_frame = ttk.Frame(main_frame)
button_frame.pack(side="left", padx=(40, 20), pady=10, fill="y")

test_run_button = ttk.Button(button_frame, text="Run Test", command=run_pytest)
test_run_button.pack(pady=16, fill="x")

analyze_button = ttk.Button(button_frame, text="Generate Report", command=run_image_similarity)
analyze_button.pack(pady=16, fill="x")

# 右側：チェックボックス（5行4列）
cb_frame = ttk.LabelFrame(main_frame, text="Test Cases", padding=16)
cb_frame.pack(side="right", padx=(20, 40), pady=10, fill="both", expand=True)

checkbox_titles = [
    "起動確認", "未ログイントップ画面", "ログイン画面", 
    "企画回選択", "買い物タブ", "必読モーダル", "パルくる便プロモ",
    "商品検索画面", "カゴタブ", "注文内容確認",
    "仮1","仮2","仮3","仮4","仮5","仮6","仮7","仮8" 
]
checkbox_vars = []
for i, title in enumerate(checkbox_titles):
    var = tk.BooleanVar()
    cb = ttk.Checkbutton(
        cb_frame,
        text=f"{title}",
        variable=var,
        style="TCheckbutton"
    )
    row = i % 5      # 5 rows
    col = i // 5     # 4 columns
    cb.grid(row=row, column=col, sticky="w", padx=16, pady=6)
    checkbox_vars.append(var)

footer = ttk.Label(root, text="© 2025 Auto Tester", font=("Segoe UI", 10), foreground="#393e46", background="#222831")
footer.pack(side="bottom", pady=12)

root.mainloop()