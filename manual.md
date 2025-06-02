# Appium＋pytest Android自動テスト手順書

## 1. 環境準備

### 必要なソフトウェア
- Python（推奨: 3.8以上）
- Appium（サーバー）
- Appium Inspector（UI要素確認用）
- Android SDK（adbコマンド利用のため）

### 必要なPythonパッケージのインストール

```sh
pip install Appium-Python-Client pytest
```

---

## 2. Appiumサーバーの起動

```sh
appium --allow-insecure=adb_shell
```

---

## 3. テスト用Android端末の準備

- USBデバッグを有効化
- `adb devices` で認識されていることを確認

---

## 4. テストコード例

```python
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

@pytest.fixture
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "実機のデバイス名"
    options.app_package = "com.example.mychat"
    options.app_activity = "com.example.mychat.MainActivity"
    options.no_reset = True

    driver = webdriver.Remote("http://localhost:4723", options=options)
    yield driver
    driver.quit()

def test_tap_by_id(driver):
    try:
        # 右上の設定ボタンをタップ
        button = driver.find_element("id", "com.example.mychat:id/setting_button")
        button_location = button.location
        print(f"Button location: {button_location['x']},{button_location['y']}")
        button.click()

        # 3秒待機
        time.sleep(3)

        # 画面のタップ（モーダルを閉じるため）
        driver.execute_script("mobile:shell", {
            "command": "input",
            "args": ["tap", str(button_location['x']), str(button_location['y'])],
            "includeStderr": True,
            "timeout": 5000
        })

        # EditTextを取得して文字列を入力
        edit_text = driver.find_element("id", "com.example.mychat:id/editText")
        edit_text.send_keys("テスト入力")

    except Exception as e:
        print("エラー内容:", e)

def test_input_text(driver):
    # EditTextに文字列を入力
    edit_text = driver.find_element("id", "com.example.mychat:id/editText")
    edit_text.send_keys("テスト入力")
    time.sleep(2)
```

---

## 5. テストの実行

```sh
pytest -s appium_test.py
```

---

## 6. Appium Inspectorの使い方

1. Appium Inspectorを起動
2. Desired Capabilitiesを入力（例: 上記テストコードと同じ内容）
3. 「Start Session」をクリック
4. 画面上の要素をクリックしてIDやXPathを確認

---

## 7. よく使う操作例

- ボタンをIDでタップ  
  `driver.find_element("id", "xxx").click()`
- テキスト入力  
  `driver.find_element("id", "xxx").send_keys("文字列")`
- 画面中央をタップ（adbコマンド利用）  
  ```python
  size = driver.get_window_size()
  x = size['width'] // 2
  y = size['height'] // 2
  driver.execute_script("mobile:shell", {
      "command": "input",
      "args": ["tap", str(x), str(y)],
      "includeStderr": True,
      "timeout": 5000
  })
  ```

---

## 8. トラブルシューティング

- **要素が見つからない**  
  → Appium InspectorでIDやXPathを再確認
- **mobile:shellでエラー**  
  → サーバー起動時に `--allow-insecure=adb_shell` を付ける
- **printが表示されない**  
  → `pytest -s` で実行

---

以上
