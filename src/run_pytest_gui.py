import tkinter as tk
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
root.geometry("800x400")
root.configure(bg="#f5f5f5")

title_label = tk.Label(root, text="自動テスト", font=("Arial", 20, "bold"), bg="#f5f5f5", fg="#333")
title_label.pack(pady=(20, 10))

main_frame = tk.Frame(root, bg="#f5f5f5")
main_frame.pack(pady=10, fill="both", expand=True)

# 左側：ボタンを縦並び
button_frame = tk.Frame(main_frame, bg="#f5f5f5")
button_frame.pack(side="left", padx=(30, 10), pady=10, fill="y")

test_run_button = tk.Button(button_frame, text="テスト実行", command=run_pytest, font=("Arial", 12), bg="#4caf50", fg="white", width=18)
test_run_button.pack(pady=10)

analyze_button = tk.Button(button_frame, text="レポート作成", command=run_image_similarity, font=("Arial", 12), bg="#2196f3", fg="white", width=18)
analyze_button.pack(pady=10)

# 右側：チェックボックス
cb_frame = tk.LabelFrame(main_frame, text="テストケース", bg="#f5f5f5", font=("Arial", 12, "bold"), fg="#666", bd=2, relief="groove", width=220)
cb_frame.pack(side="right", padx=(10, 30), pady=10, fill="both", expand=True)

checkbox_titles = [
    "起動確認", "未ログイントップ画面", "ログイン画面", 
    "企画回選択", "買い物タブ", "必読モーダル", "パルくる便プロモ",
    "商品検索画面", "カゴタブ", "注文内容確認",
    "仮1","仮2","仮3","仮4","仮5","仮6","仮7","仮8" 
]
checkbox_vars = []
for i, title in enumerate(checkbox_titles):
    var = tk.BooleanVar()
    cb = tk.Checkbutton(cb_frame, text=title, variable=var, bg="#f5f5f5", font=("Arial", 10), anchor="w")
    row = i % 5      # 5行
    col = i // 5     # 4列
    cb.grid(row=row, column=col, sticky="w", padx=10, pady=2)
    checkbox_vars.append(var)

footer = tk.Label(root, text="© 2025 Auto Tester", bg="#f5f5f5", fg="#aaa", font=("Arial", 9))
footer.pack(side="bottom", pady=10)

root.mainloop()