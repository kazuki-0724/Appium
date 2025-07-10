# Appium＋pytest Android自動テスト

### 1. Appiumサーバの起動

```sh
appium --allow-insecure=adb_shell
```

## 2. GUIの起動
```sh
python run_pytest_gui.py
```

### 3. テストケースのコマンド実行
```sh
pytest -s appium_palapp_test.py -k 実行したいテストのメソッド
pytest -s appium_palapp_test.py -k test_no_login_top
```

### 4. テスト結果評価
```sh
python image_similarity.py
```
