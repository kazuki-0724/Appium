import sys
import subprocess
import threading

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
    ("起動確認", "test_splash"),
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
        app.postEvent(window, lambda: QMessageBox.information(window, "完了", "テストが完了しました。"))

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