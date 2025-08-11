from common.common_const import WaitTime
from common.common_command import CommonCommand
import time
from common.common_const import Direction

class OrderConfirm(CommonCommand):

    ORDER_CONFIRM = "button_order_confirm"
    
    def do_test(self,driver):
        try:
            # 注文内容確認
            self.tap_button(driver, self.TAB_CART)
            self.tap_button(driver, self.ORDER_CONFIRM)
            self.save_screenshot_with_date(driver, "order_confirm_375.png")
            
            # 【画面制御】
            # 「←」をタップする
            self.tap_back_button(driver)
            self.save_screenshot_with_date(driver, "order_confirm_377.png")

            # 増資の「？」をタップする
            self.tap_button(driver, self.ORDER_CONFIRM)
            self.long_tap(driver, 0.158, 0.435, 200)
            self.save_screenshot_with_date(driver, "order_confirm_379.png")

            # 「X」をタップする
            self.sleep(WaitTime.LONG.value)
            self.tap_close_button(driver)
            self.save_screenshot_with_date(driver, "order_confirm_380.png")



            #【増資変更】
            # 増資額の「変更」をタップする
            self.long_tap(driver, 0.894, 0.438, 200)
            self.save_screenshot_with_date(driver, "order_confirm_382.png")
            
            # 100円の数量を「10」に設定する
            self.long_tap(driver, 0.841, 0.175, 200)
            # 「1」をタップする
            self.tap_anywhere(driver, 0.137, 0.721)
            # 「0」をタップする
            self.tap_anywhere(driver, 0.379, 0.924)
            self.save_screenshot_with_date(driver, "order_confirm_384-1.png")

            # 「キャンセル」をタップする
            self.long_tap(driver, 0.401, 0.382, 200)
            self.save_screenshot_with_date(driver, "order_confirm_384-2.png")

            
            # 増資額の「変更」をタップする
            self.long_tap(driver, 0.894, .438, 200)
            self.save_screenshot_with_date(driver, "order_confirm_385.png")
            
            # 100円の数量を「10」に設定する
            self.long_tap(driver, 0.841, 0.175, 200)
            # 「1」をタップする
            self.tap_anywhere(driver, 0.137, 0.721)
            # 「0」をタップする
            self.tap_anywhere(driver, 0.379, 0.924)
            self.save_screenshot_with_date(driver, "order_confirm_387-1.png")

            # 「←」をタップする
            self.tap_back_button(driver)
            self.save_screenshot_with_date(driver, "order_confirm_387-2.png")


            # 増資額の「変更」をタップする
            self.long_tap(driver, 0.894, .438, 200)
            self.save_screenshot_with_date(driver, "order_confirm_388.png")
            
            # 100円の数量を「10」に設定する
            self.long_tap(driver, 0.841, 0.175, 200)
            # 「1」をタップする
            self.tap_anywhere(driver, 0.137, 0.721)
            # 「0」をタップする
            self.tap_anywhere(driver, 0.379, 0.924)
            self.save_screenshot_with_date(driver, "order_confirm_390.png")

            # 「変更する」をタップする
            self.long_tap(driver, 0.658, 0.382, 200)
            self.save_screenshot_with_date(driver, "order_confirm_391.png")




            #【利用ポイント変更】
            # 利用ポイントの「変更」をタップする
            self.long_tap(driver, 0.894, 0.500, 200)
            self.save_screenshot_with_date(driver, "order_confirm_392.png")
            
            # 100Pの数量を「10」に設定する
            self.long_tap(driver, 0.710, 815/2412, 200)
            # 「1」をタップする
            self.tap_anywhere(driver, 0.137, 0.721)
            # 「0」をタップする
            self.tap_anywhere(driver, 0.379, 0.924)
            # 一度フォーカスを外す
            self.long_tap(driver, 0.379, 0.124, 200)
            self.save_screenshot_with_date(driver, "order_confirm_393.png")

            # 「キャンセル」をタップする
            # 「キャンセル」が見えるまでスワイプ（一番下）
            self.swipe_vertical(driver, 800, Direction.UP.value)
            self.swipe_vertical(driver, 800, Direction.UP.value)
            self.long_tap(driver, 0.495, 0.814, 200)
            self.save_screenshot_with_date(driver, "order_confirm_394.png")

            
            # 利用ポイントの「変更」をタップする
            self.long_tap(driver, 0.894, 0.500, 200)
            self.save_screenshot_with_date(driver, "order_confirm_395.png")
            
            # 100Pの数量を「10」に設定する
            self.long_tap(driver, 0.710, 815/2412, 200)
            # 「1」をタップする
            self.tap_anywhere(driver, 0.137, 0.721)
            # 「0」をタップする
            self.tap_anywhere(driver, 0.379, 0.924)
            self.save_screenshot_with_date(driver, "order_confirm_396.png")

            # 「←」をタップする
            self.tap_back_button(driver)
            self.save_screenshot_with_date(driver, "order_confirm_397.png")


            # 利用ポイントの「変更」をタップする
            self.long_tap(driver, 0.894, 0.500, 200)
            self.save_screenshot_with_date(driver, "order_confirm_398.png")
            
            # 100Pの数量を「10」に設定する
            self.long_tap(driver, 0.710, 815/2412, 200)
            # 「1」をタップする
            self.tap_anywhere(driver, 0.137, 0.721)
            # 「0」をタップする
            self.tap_anywhere(driver, 0.379, 0.924)
            self.save_screenshot_with_date(driver, "order_confirm_399-1.png")

            # 一度フォーカスを外す
            self.long_tap(driver, 0.379, 0.124, 200)
            # 「ポイントを使用する」をタップする
            # 「ポイントを使用する」が見えるまでスワイプ（一番下）
            self.swipe_vertical(driver, 800, Direction.UP.value)
            self.swipe_vertical(driver, 800, Direction.UP.value)
            self.save_screenshot_with_date(driver, "order_confirm_399-2.png")

            # 「ポイントを使用する」をタップする
            self.long_tap(driver, 0.495, 0.747, 200)
            self.save_screenshot_with_date(driver, "order_confirm_400.png")

        except Exception as e:
            print("エラー内容:", e)