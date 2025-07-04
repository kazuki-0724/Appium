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