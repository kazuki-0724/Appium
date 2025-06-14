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

## 2. テストコードの仕組み
### CommonCommandをベースクラスとして、基本操作を定義している。
基本操作：絶対座標
1. タップ
2. 長押し
3. スクロール
4. スワイプ
5. スクロール

### 基本操作：UI部品
1. ボタンクリック
2. テキスト入力

各テストケースは上記の基本操作を組み合わせて実現している


---

## 3. テストの準備

- 開発者オプションからUSBデバッグを有効化
- テストに使用する組合員についてデータの準備を行う

---


## 4. テストの実行

1. Appiumサーバを起動する
2. pytestコマンドでテストケースを実行する

```sh
appium --allow-insecure=adb_shell
pytest -s appium_palapp_test.py
```

---

## 5. テストの評価

1. 評価処理を実行する
```sh
python image_similarity.py
```

2. テスト結果の確認
テスト実行時のスクリーンショットは「YYYYMMDD」のフォルダに保存されている。
各テストケースの結果は「report〇.html」にて確認できる。
正しいテスト結果のスクリーンショットと実行結果のスクリーンショットをピクセル単位で比較する。

---


## 6. Appium Inspectorの使い方

1. Appium Inspectorを起動
2. Desired Capabilitiesを入力（例: 上記テストコードと同じ内容）
3. 「Start Session」をクリック
4. 画面上の要素をクリックしてIDやXPathを確認

---
