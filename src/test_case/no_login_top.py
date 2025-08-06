from common.common_const import WaitTime
from common.common_command import CommonCommand
import time
from datetime import datetime
from common.common_const import Direction

class NoLoginTop(CommonCommand):
    
    # パーツID
    CREATE_ACCOUNT = "goto_creat_account_btn"
    CONTENTS = "contents_imageview"
    LEFT = "back_icon_imageview"
    RIGHT = "forward_icon_imageview"
    GO_LOGIN = "goto_login_btn"
    
    
    def do_test(self,driver):
        try:
            # 未ログイントップ
            self.save_screenshot_with_date(driver, "no_login_top_007.png")

            self.swipe_contents_horizontaly(driver, 250, Direction.RIGHT.value)
            self.save_screenshot_with_date(driver, "no_login_top_010.png")

            self.swipe_contents_horizontaly(driver, 250, Direction.LEFT.value)
            self.save_screenshot_with_date(driver, "no_login_top_011.png")

            self.tap_button(driver, NoLoginTop.RIGHT, WaitTime.SHORT.value)
            self.save_screenshot_with_date(driver, "no_login_top_012.png")

            self.tap_button(driver, NoLoginTop.RIGHT, WaitTime.SHORT.value)
            self.save_screenshot_with_date(driver, "no_login_top_016.png")

            self.swipe_contents_horizontaly(driver, 250, Direction.LEFT.value)
            self.save_screenshot_with_date(driver, "no_login_top_019.png")

            self.swipe_contents_horizontaly(driver, 250, Direction.RIGHT.value)
            self.save_screenshot_with_date(driver, "no_login_top_020.png")

            self.tap_button(driver, NoLoginTop.LEFT, WaitTime.SHORT.value)
            self.save_screenshot_with_date(driver, "no_login_top_021.png")
            
            # 「アカウントを作成する」をタップする
            self.tap_button(driver, NoLoginTop.CREATE_ACCOUNT, WaitTime.SHORT.value)
            self.save_screenshot_with_date(driver, "no_login_top_022.png")
            
            # 「よくあるお問い合わせ」をタップする
            self.long_tap(driver, 0.380, 0.793, 200)
            #self.save_screenshot_with_date(driver, "no_login_top_023.png")
            self.long_tap(driver, 0.644, 0.615, 200)
            self.save_screenshot_with_date(driver, "no_login_top_023.png")
            
            # 「X」をタップする
            self.tap_button(driver, self.HEADER_CLOSE)
            self.save_screenshot_with_date(driver, "no_login_top_024.png")
            
            # 「組合員番号」をタップする
            self.long_tap(driver, 0.168, 0.420, 200)
            # 「5」をタップする
            self.tap_anywhere(driver, 0.378, 0.784)
            # 「電話番号」をタップする
            self.long_tap(driver, 0.168, 0.568, 200)
            #「5」をタップする　x10
            self.tap_anywhere(driver, 0.378, 0.784)
            self.tap_anywhere(driver, 0.378, 0.784)
            self.tap_anywhere(driver, 0.378, 0.784)
            self.tap_anywhere(driver, 0.378, 0.784)
            self.tap_anywhere(driver, 0.378, 0.784)
            self.tap_anywhere(driver, 0.378, 0.784)
            self.tap_anywhere(driver, 0.378, 0.784)
            self.tap_anywhere(driver, 0.378, 0.784)
            self.tap_anywhere(driver, 0.378, 0.784)
            self.tap_anywhere(driver, 0.378, 0.784)
            # 領域外タップでキーボードを閉じる
            self.long_tap(driver, 0.800, 0.568, 200)
            
            # 確認コードを送信する
            self.long_tap(driver, 0.166, 0.814, 200)
            self.save_screenshot_with_date(driver, "no_login_top_025.png")
            
            # キャンセルをタップする
            self.long_tap(driver, 0.639, 0.609, 200)
            self.save_screenshot_with_date(driver, "no_login_top_026.png")
            
            # 「←」をタップする
            self.tap_button(driver, self.BACK)
            self.save_screenshot_with_date(driver, "no_login_top_036.png")
            
            # 「ログインへ進む」をタップする
            self.tap_button(driver, NoLoginTop.GO_LOGIN, WaitTime.SHORT.value)

        except Exception as e:
            print("エラー内容:", e)
            
    
    # 任意の変化量でスワイプを実行する関数
    def swipe_contents_horizontaly(self, driver, diff, direction, sleep_time=WaitTime.SHORT.value):
        time.sleep(sleep_time)
        size = driver.get_window_size()
        # 中心座標を取得
        x = size['width'] // 2
        y = 0.665 * size['height']

        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] swipe horizontal from {x} to {x + 400} at {y}")

        driver.execute_script("mobile: swipeGesture", {
            "left": x,
            "top": y,
            "width": diff,
            "height": 0,
            "direction": direction,
            "percent": 1.0
        })