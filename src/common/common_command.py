import time
from datetime import datetime
import os
from common.common_const import WaitTime

class CommonCommand:

    # パーツID
    BACK = "image_button_back"
    HEADER_FEE_TOTAL = "total_fee_text"
    HEADER_CATALOG = "image_button_catalog"
    HEADER_SEARCH = "image_button_search"
    HEADER_CATEGORY = "image_button_category"
    HEADER_CLOSE = "image_button_close"
    TAB_SHOPPING = "shopping_button"
    TAB_CART = "cart_button"
    TAB_DELIVERY = "delivery_button"
    TAB_MENU = "menu_button"

    # NP：1080x2412
    # 相対座標から絶対座標に変換する関数
    def convert_to_device_coordinates(self, driver, rx, ry):
        x = driver.get_window_size()['width'] *rx
        y = driver.get_window_size()['height'] * ry
        return [int(x), int(y)]


    # 要素のtextを表示する関数
    def check_element_text(self, driver, element_id):
        try:
            time.sleep(WaitTime.LONG.value)
            element = driver.find_element("id", "jp.co.pal_system.pochipal:id/" + element_id)
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] element text is {element.text}")
        except Exception as e:
            print(f"Element with ID '{element_id}' not found: {e}")
            return None


    # スリープ関数
    def sleep(self, seconds):
        time.sleep(seconds)


    # スクリーンショットを取得する関数
    def save_screenshot_with_date(self, driver, filename="screenshot.png", directory="screenshot", wait_time=WaitTime.SHORT.value):
        time.sleep(wait_time)
        # 保存先を ../reports/screenshot に変更
        folder = os.path.join("..", "reports", directory)
        if not os.path.exists(folder):
            os.makedirs(folder)
        # フォルダ内にスクリーンショットを保存
        filepath = os.path.join(folder, filename)
        driver.save_screenshot(filepath)
        print(f"スクリーンショットを保存しました: {filepath}")


    # ボタンをタップする関数
    def tap_button(self, driver, button_id, sleep_time=WaitTime.SHORT.value):
        time.sleep(sleep_time)
        driver.find_element("id", "jp.co.pal_system.pochipal:id/"+button_id).click()
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {button_id} tapped")
    

    # 戻るボタンをタップする関数
    def tap_back_button(self, driver, sleep_time=WaitTime.SHORT.value):
        time.sleep(sleep_time)
        driver.find_element("id", "jp.co.pal_system.pochipal:id/"+CommonCommand.BACK).click()
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Back button tapped")


    # 戻るボタンをタップする関数
    def tap_close_button(self, driver, sleep_time=WaitTime.SHORT.value):
        time.sleep(sleep_time)
        driver.find_element("id", "jp.co.pal_system.pochipal:id/"+CommonCommand.HEADER_CLOSE).click()
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] close button tapped")


    # 文字を入力する関数
    def input_text(self, driver, element_id, text, sleep_time=WaitTime.SHORT.value):
        time.sleep(sleep_time)
        element = driver.find_element("id", "jp.co.pal_system.pochipal:id/"+element_id)
        element.clear()
        element.send_keys(text)
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Input text '{text}' into {element_id}")


    # 任意の座標をタップする関数
    def tap_anywhere(self, driver, x, y):
        coordinates = self.convert_to_device_coordinates(driver, x, y)
        x , y = coordinates[0], coordinates[1]

        time.sleep(WaitTime.LONG.value)
        driver.execute_script("mobile:shell", {
            "command": "input",
            "args": ["tap", str(x), str(y)],
            "includeStderr": True,
            "timeout": 5000
        })
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Tapped at ({x}, {y})")


    def long_tap(self, driver, x, y, duration_ms=500):
        coordinates = self.convert_to_device_coordinates(driver, x, y)
        x , y = coordinates[0], coordinates[1]
        time.sleep(WaitTime.LONG.value)
        driver.execute_script("mobile: longClickGesture", {
            "x": x,
            "y": y,
            "duration": duration_ms  # ミリ秒単位
        })
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Long Tapped at ({x}, {y})")


    # 任意の変化量でスワイプを実行する関数
    def swipe_vertical(self, driver, diff, direction, sleep_time=WaitTime.SHORT.value):
        time.sleep(sleep_time)
        size = driver.get_window_size()
        # 中心座標を取得
        x = size['width'] // 2
        y = size['height'] // 4

        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] swipe ({diff})")

        driver.execute_script("mobile: swipeGesture", {
            "left": x,
            "top": y,
            "width": 0,
            "height": diff,
            "direction": direction,
            "percent": 1.0
        })


    # 任意の変化量でスクロールを実行する関数
    def scroll_vertical(self, driver, diff, direction, sleep_time=WaitTime.SHORT.value):
        time.sleep(sleep_time)
        size = driver.get_window_size()
        # 中心座標を取得
        x = size['width'] // 2
        y = size['height'] // 2

        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] scroll ({diff})")
    
        driver.execute_script("mobile: scrollGesture", {
            "left": x,
            "top": y,
            "width": 0,
            "height": diff,
            "direction": direction,
            "percent": 1.0
        })


    # カートを空にする関数
    # 通常商品で削除グレーアウトになっていない商品であればまとめて削除できる
    def clear_cart(self, driver):
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ■ CLEAR CART START")
        while True:
            # 金額を確認する
            element = driver.find_element("id", "jp.co.pal_system.pochipal:id/" + self.HEADER_FEE_TOTAL)
            if "0円(税込)" == element.text:
                 break
            else:
                # 一度カゴ画面に遷移
                self.tap_button(driver, self.TAB_CART)
                # 通常商品のみの前提で一番上部にある商品を削除
                self.long_tap(driver, 0.121, 0.364, 200)
                # 「削除」をタップ
                self.tap_anywhere(driver, 0.673, 0.944)
                # 「x」をタップ
                self.tap_button(driver, self.HEADER_CLOSE)
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ■ CLEAR CART END")
         
