# ディレクトリ: Appium/src

---

### ファイル: Appium/src/appium_palapp_test.py

```python
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
import time
from common.common_command import CommonCommand
from test_case.no_login_top import NoLoginTop
from test_case.login import Login
from test_case.account_create import AccountCreate
from test_case.splash import Splash
from test_case.shopping_tab import ShoppingTab
from test_case.item_search import ItemSearch
from test_case.select_product_catalog import SelectProductCatalog
from test_case.parukuru_promotion import PalPromo
from test_case.must_read_modal import MustReadModal
from test_case.cart import Cart
from test_case.order_confirm import OrderConfirm
from test_case.order_complete import OrderComplete
from common.common_command import CommonCommand


@pytest.fixture
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "84607e4c"
    options.app_package = "jp.co.pal_system.pochipal"
    options.app_activity = "jp.co.pal_system.pochipal.main.activity.SplashActivity"
    options.no_reset = True
    driver = webdriver.Remote("http://localhost:4723", options=options)
    yield driver
    driver.quit()


# テストケース(先頭にtest_をつける)
def test_all_case(driver):
    try:
        print("\n#テスト開始######################################")

        # スプラッシュ画面
        Splash().do_test(driver)
        # 必読モーダル
        MustReadModal().do_test(driver)
        # パルくる便プロモ
        PalPromo().do_test(driver)
        # 未ログイントップ
        NoLoginTop().do_test(driver)
        # アカウント設定
        AccountCreate().do_test(driver)
        # ログイン画面
        Login().do_test(driver)
        # 通知権限の許可（座標は端末により調整）
        CommonCommand().tap_anywhere(driver, 0.498, 0.550)
        time.sleep(3)
        # 企画回選択
        SelectProductCatalog().do_test(driver)
        time.sleep(3)
        # 買い物タブ
        ShoppingTab().do_test(driver)
        # 商品検索画面
        ItemSearch().do_test(driver)
        # カゴ画面
        Cart().do_test(driver)
        # 注文内容確認確認
        OrderConfirm().do_test(driver)
        # 送信完了画面
        OrderComplete().do_test(driver)


        print("\n#テスト終了######################################")
    
    except Exception as e:
        print("エラー内容:", e)


# 各テストケースを単独で実行するメソッド
def test_splash(driver):
    try:
        print("\n#スプラッシュ画面テスト開始######################################")
        Splash().do_test(driver)
        print("\n#スプラッシュ画面テスト終了######################################")
    except Exception as e:
        print("エラー内容:", e)


def test_must_read_modal(driver):
    try:
        print("\n#必読モーダルテスト開始######################################")
        MustReadModal().do_test(driver)
        print("\n#必読モーダルテスト終了######################################")
    except Exception as e:
        print("エラー内容:", e)


def test_parukuru_promotion(driver):
    try:
        print("\n#パルくる便プロモテスト開始######################################")
        PalPromo().do_test(driver)
        print("\n#パルくる便プロモテスト終了######################################")
    except Exception as e:
        print("エラー内容:", e)


def test_no_login_top(driver):
    try:
        print("\n#未ログイントップテスト開始######################################")
        NoLoginTop().do_test(driver)
        print("\n#未ログイントップテスト終了######################################")
    except Exception as e:
        print("エラー内容:", e)


def test_account_create(driver):
    try:
        print("\n#アカウント作成テスト開始######################################")
        AccountCreate().do_test(driver)
        print("\n#アカウント作成テスト終了######################################")
    except Exception as e:
        print("エラー内容:", e)


def test_login(driver):
    try:
        print("\n#ログイン画面テスト開始######################################")
        Login().do_test(driver)
        print("\n#ログイン画面テスト終了######################################")
    except Exception as e:
        print("エラー内容:", e)


def test_select_product_catalog(driver):
    try:
        print("\n#企画回選択テスト開始######################################")
        SelectProductCatalog().do_test(driver)
        print("\n#企画回選択テスト終了######################################")
    except Exception as e:
        print("エラー内容:", e)


def test_shopping_tab(driver):
    try:
        print("\n#買い物タブテスト開始######################################")
        ShoppingTab().do_test(driver)
        print("\n#買い物タブテスト終了######################################")
    except Exception as e:
        print("エラー内容:", e)


def test_item_search(driver):
    try:
        print("\n#商品検索画面テスト開始######################################")
        ItemSearch().do_test(driver)
        print("\n#商品検索画面テスト終了######################################")
    except Exception as e:
        print("エラー内容:", e)


def test_cart(driver):
    try:
        print("\n#カゴ画面テスト開始######################################")
        Cart().do_test(driver)
        print("\n#カゴ画面テスト終了######################################")
    except Exception as e:
        print("エラー内容:", e)


def test_order_confirm(driver):
    try:
        print("\n#注文内容確認テスト開始######################################")
        OrderConfirm().do_test(driver)
        print("\n#注文内容確認テスト終了######################################")
    except Exception as e:
        print("エラー内容:", e)


def test_order_complete(driver):
    try:
        print("\n#注文完了画面テスト開始######################################")
        OrderComplete().do_test(driver)
        print("\n#注文完了画面テスト終了######################################")
    except Exception as e:
        print("エラー内容:", e)


def test_sample_case(driver):
    try:
        print("\n#サンプルテスト開始######################################")
        OrderComplete().do_test(driver)
        print("\n#サンプルテスト終了######################################")
    
    except Exception as e:
        print("エラー内容:", e)
```

---

### ファイル: Appium/src/image_similarity.py

```python
import os
from PIL import Image, ImageChops
import numpy as np
import re
from bs4 import BeautifulSoup

# === 各種パス・ファイルリストの準備 ===

# テスト実行時のスクリーンショット格納フォルダ
current_folder = "../reports/screenshot"
# 正解（期待値）スクリーンショット格納フォルダ
collect_folder = "../reports/dummy"
# テンプレートHTML（各テストケースごと）のリスト
html_files = [f"../reports/template/report{i}.html" for i in range(1, 10)]
# 出力先ディレクトリ
output_dir = "../reports/generated"
# summary.htmlのパス
summary_path = os.path.join(output_dir, "summary.html")

# スクリーンショットファイル名の集合を取得
current_artifacts = set(os.listdir(current_folder))
collect_artifacts = set(os.listdir(collect_folder))
# 両方に存在するファイルのみ比較対象とする
common_files = current_artifacts & collect_artifacts

# 類似度結果を格納する辞書
similarity_dict = {}

# === 画像比較処理 ===
for filename in common_files:
    # path1: テスト実行時の画像, path2: 正解画像
    path1 = os.path.join(current_folder, filename)
    path2 = os.path.join(collect_folder, filename)
    
    try:
        # 画像をRGBで開く
        img1 = Image.open(path1).convert("RGB")
        img2 = Image.open(path2).convert("RGB")
        # 画像サイズが異なる場合は「サイズ不一致」とする
        if img1.size != img2.size:
            similarity = "サイズ不一致"
        else:
            # 差分画像を計算
            diff = ImageChops.difference(img1, img2)
            diff_np = np.array(diff)
            # 完全一致なら1.0000
            if np.all(diff_np == 0):
                similarity = "1.0000"
            else:
                # 一致率を計算し、1.0未満ならNG表記
                sim = 1 - (np.count_nonzero(diff_np) / diff_np.size)
                if sim == 1.0:
                    similarity = "1.0000"
                else:
                    similarity = f"NG：{sim*100:.2f}%"
        # ファイル名からキー（例: 123や123-1など）を抽出
        base = os.path.splitext(filename)[0]
        m = re.search(r'(\d{3}(?:-\d+)?)$', base)
        if m:
            key = m.group(1)
        else:
            key = base
        # 類似度を辞書に格納
        similarity_dict[key] = similarity
    except Exception as e:
        print(f"{filename}: 比較エラー {e}")

# === テンプレートHTMLの類似度埋め込み・保存 ===

# 出力ディレクトリがなければ作成
os.makedirs(output_dir, exist_ok=True)

# {similarity_XXX} を対応する値で置換する関数
def replace_similarity(match):
    key = match.group(1)
    return similarity_dict.get(key, "N/A")

# 各レポートのNG判定リスト
report_ng = []

for idx, html_path in enumerate(html_files, 1):
    if not os.path.exists(html_path):
        print(f"{html_path} が見つかりません。スキップします。")
        report_ng.append(True)  # ファイルがなければ失敗扱い
        continue
    with open(html_path, encoding="utf-8") as f:
        html = f.read()
    # {similarity_XXX} を実際の値で置換
    html = re.sub(r"\{similarity_([0-9]{3}(?:-\d+)?)\}", replace_similarity, html)
    # 埋め込んだ後のHTMLから類似度値を抽出し、1.0000以外があればNG
    similarities = re.findall(r'>(1\.0000|NG：[\d\.]+%|サイズ不一致)<', html)
    has_ng = any(s != "1.0000" for s in similarities)
    report_ng.append(has_ng)
    # 埋め込み済みHTMLをgeneratedディレクトリに保存
    output_path = os.path.join(output_dir, os.path.basename(html_path))
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"{output_path} に埋め込み済みHTMLを保存しました。")

# === summary.htmlの「成功」「失敗」書き換え ===
if os.path.exists(summary_path):
    with open(summary_path, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    # 各reportXのidを「失敗」または「成功」に書き換え
    for i, ng in enumerate(report_ng, 1):
        tag = soup.find(id=f"report{i}")
        if tag:
            if ng:
                tag.string = "失敗"
                tag["class"] = "status-fail"
            else:
                tag.string = "成功"
                tag["class"] = "status-success"
    # summary.htmlを上書き保存
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write(str(soup))
    print("summary.htmlを更新しました。")
else:
    print("summary.htmlが見つかりません。更新をスキップします。")
```

---

### ファイル: Appium/src/run_pytest_gui.py

```python
import sys
import subprocess
import threading
from PyQt5.QtCore import QTimer

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QCheckBox, QGroupBox, QMessageBox, QGridLayout, QFrame
)
from PyQt5.QtGui import QFont, QColor, QPalette, QIcon
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)

# ダークテーマ風パレット
palette = QPalette()
palette.setColor(QPalette.Window, QColor("#222831"))
palette.setColor(QPalette.WindowText, QColor("#eeeeee"))
palette.setColor(QPalette.Base, QColor("#232931"))
palette.setColor(QPalette.AlternateBase, QColor("#393e46"))
palette.setColor(QPalette.ToolTipBase, QColor("#ffd600"))
palette.setColor(QPalette.ToolTipText, QColor("#222831"))
palette.setColor(QPalette.Text, QColor("#eeeeee"))
palette.setColor(QPalette.Button, QColor("#00adb5"))
palette.setColor(QPalette.ButtonText, QColor("#eeeeee"))
palette.setColor(QPalette.Highlight, QColor("#ffd600"))
palette.setColor(QPalette.HighlightedText, QColor("#222831"))
app.setPalette(palette)

window = QWidget()
window.setWindowTitle("Auto Tester")
window.setWindowIcon(QIcon())  # アイコンを設定したい場合はここにパス
window.resize(820, 480)

main_layout = QVBoxLayout(window)
main_layout.setContentsMargins(32, 32, 32, 20)
main_layout.setSpacing(18)

# タイトル
title = QLabel("Auto Tester")
title.setFont(QFont("Segoe UI", 28, QFont.Bold))
title.setStyleSheet("""
    color: #00adb5;
    letter-spacing: 0.08em;
    padding-bottom: 8px;
""")
title.setAlignment(Qt.AlignCenter)
main_layout.addWidget(title)

# セパレーター
sep = QFrame()
sep.setFrameShape(QFrame.HLine)
sep.setFrameShadow(QFrame.Sunken)
sep.setStyleSheet("color: #393e46; background: #393e46; min-height:2px;")
main_layout.addWidget(sep)

content_layout = QHBoxLayout()
content_layout.setSpacing(32)
main_layout.addLayout(content_layout)

# 左側：ボタン
button_layout = QVBoxLayout()
button_layout.setSpacing(28)

# チェックボックスタイトルとpytestの-k引数用キーワードの対応リスト
checkbox_titles = [
    ("スプラッシュ画面", "test_splash"),
    ("未ログイントップ画面", "test_no_login_top"),
    ("ログイン画面", "test_login"),
    ("企画回選択", "test_select_product_catalog"),
    ("買い物タブ", "test_shopping_tab"),
    ("必読モーダル", "test_must_read_modal"),
    ("パルくる便プロモ", "test_parukuru_promotion"),
    ("商品検索画面", "test_item_search"),
    ("カゴタブ", "test_cart"),
    ("注文内容確認", "test_order_confirm"),
    ("アカウント作成", "test_account_create"),
    ("注文完了", "test_order_complete"),
    # 必要に応じて追加
]

checkbox_labels = [t[0] for t in checkbox_titles]
checkbox_keywords = [t[1] for t in checkbox_titles]

checkboxes = []

def run_pytest():
    selected = [checkbox_keywords[i] for i, cb in enumerate(checkboxes) if cb.isChecked()]
    if not selected:
        QMessageBox.warning(window, "警告", "実行するテストを選択してください。")
        return
    k_expr = " or ".join(selected)
    cmd = ["pytest", "-s", "appium_palapp_test.py", "-k", k_expr]

    def task():
        subprocess.run(cmd, cwd="c:/programs/GitHubWS/Appium/src")
        # メインスレッドでメッセージボックスを表示
        QTimer.singleShot(0, lambda: QMessageBox.information(None, "完了", "テストが完了しました。"))

    threading.Thread(target=task, daemon=True).start()

def run_image_similarity():
    subprocess.run(["python", "image_similarity.py"], cwd="c:/programs/GitHubWS/Appium/src")
    QMessageBox.information(window, "完了", "レポート作成が完了しました。")

run_btn = QPushButton("テスト実行")
run_btn.setFont(QFont("Segoe UI", 13, QFont.Bold))
run_btn.setCursor(Qt.PointingHandCursor)
run_btn.setStyleSheet("""
    QPushButton {
        background-color: #00adb5;
        color: #eeeeee;
        padding: 16px 0;
        border-radius: 10px;
        font-size: 1.1em;
    }
    QPushButton:hover {
        background-color: #00cfc1;
        color: #222831;
    }
""")
run_btn.clicked.connect(run_pytest)
button_layout.addWidget(run_btn)

report_btn = QPushButton("レポート生成")
report_btn.setFont(QFont("Segoe UI", 13, QFont.Bold))
report_btn.setCursor(Qt.PointingHandCursor)
report_btn.setStyleSheet("""
    QPushButton {
        background-color: #00adb5;
        color: #eeeeee;
        padding: 16px 0;
        border-radius: 10px;
        font-size: 1.1em;
    }
    QPushButton:hover {
        background-color: #ffd600;
        color: #222831;
    }
""")
report_btn.clicked.connect(run_image_similarity)
button_layout.addWidget(report_btn)
button_layout.addStretch()
content_layout.addLayout(button_layout, 1)

# 右側：チェックボックス
cb_group = QGroupBox("Test Cases")
cb_group.setFont(QFont("Segoe UI", 13, QFont.Bold))
cb_group.setStyleSheet("""
    QGroupBox {
        color: #00adb5;
        border: 2px solid #00adb5;
        border-radius: 12px;
        margin-top: 10px;
        background: #232931;
        padding: 10px 10px 10px 10px;
    }
    QGroupBox:title {
        subcontrol-origin: margin;
        left: 16px;
        padding: 0 8px 0 8px;
    }
""")
cb_layout = QGridLayout()
cb_group.setLayout(cb_layout)

for i, label in enumerate(checkbox_labels):
    cb = QCheckBox(label)
    cb.setFont(QFont("Meiryo", 11))
    cb.setStyleSheet("""
        QCheckBox {
            color: #ffd600;
            spacing: 8px;
            padding: 6px 0;
        }
        QCheckBox::indicator {
            width: 22px;
            height: 22px;
            border-radius: 6px;
            border: 2px solid #00adb5;
            background: #232931;
        }
        QCheckBox::indicator:checked {
            background: #00adb5;
            border: 2px solid #ffd600;
        }
    """)
    row = i % 6
    col = i // 6
    cb_layout.addWidget(cb, row, col)
    checkboxes.append(cb)
content_layout.addWidget(cb_group, 2)

# フッター
footer = QLabel("© 2025 Auto Tester")
footer.setFont(QFont("Segoe UI", 10))
footer.setStyleSheet("color: #393e46; background: #222831; padding-top: 8px;")
footer.setAlignment(Qt.AlignCenter)

main_layout.addWidget(footer)

window.show()

sys.exit(app.exec_())
```

