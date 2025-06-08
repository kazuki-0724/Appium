from common.common_const import WaitTime
from common.common_command import CommonCommand
import time
from common.common_const import Direction

class MustReadModal(CommonCommand):

    # パーツID
    CONFIRM_CHECKBOX = "confirm_checkbox_text"
    CLOSE_BTN = "closeBtn"
    

    def do_test(self,driver):
        try:
            # 必読モーダル
            time.sleep(2)
            # 上記表示確認
            self.save_screenshot_with_date(driver, "must_read_modal_112.png")
            
            # 下部まで移動
            self.swipe_vertical(driver, 500, Direction.UP.value)
            self.save_screenshot_with_date(driver, "must_read_modal_113.png")

            # チェックボックスをチェック
            self.tap_button(driver, self.CONFIRM_CHECKBOX, WaitTime.SHORT.value)
            self.save_screenshot_with_date(driver, "must_read_modal_117.png")
            
            # 上部まで移動
            self.swipe_vertical(driver, 500, Direction.DOWN.value)
            self.save_screenshot_with_date(driver, "must_read_modal_118.png")

            # 下部まで移動
            self.swipe_vertical(driver, 500, Direction.UP.value)
            self.save_screenshot_with_date(driver, "must_read_modal_119.png")

            # チェックボックスをチェックアウト
            self.tap_button(driver, self.CONFIRM_CHECKBOX, WaitTime.SHORT.value)
            self.save_screenshot_with_date(driver, "must_read_modal_121.png")

            # チェックボックスをチェック
            self.tap_button(driver, self.CONFIRM_CHECKBOX, WaitTime.SHORT.value)
            self.save_screenshot_with_date(driver, "must_read_modal_123.png")

            # 領域外タップ
            self.long_tap(driver, 0.880, 0.963,200)
            self.save_screenshot_with_date(driver, "must_read_modal_124.png")

            # チェックボックスをチェック
            self.tap_button(driver, self.CLOSE_BTN, WaitTime.SHORT.value)
            self.save_screenshot_with_date(driver, "must_read_modal_125.png")
            
        except Exception as e:
            print("エラー内容:", e)