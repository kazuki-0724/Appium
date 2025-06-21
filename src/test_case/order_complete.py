from common.common_const import WaitTime
from common.common_command import CommonCommand
import time
from common.common_const import Direction

class OrderComplete(CommonCommand):

    ORDER_COMPLETE = "button_order_complete"
    ORDER_CONTINUE = "button_continue_shopping"
    SELECT_BUTTON = "productCatalogSelectBtn"
    
    def do_test(self,driver):
        try:
            # 注文完了画面
            # self.tap_button(driver, self.TAB_CART)
            self.tap_button(driver, self.ORDER_COMPLETE)
            self.save_screenshot_with_date(driver, "order_complete_402.png")

            # 「注文を続ける」をタップする
            self.tap_button(driver, self.ORDER_CONTINUE)
            self.save_screenshot_with_date(driver, "order_complete_408.png")
            
            # 6月1回の企画回を選択
            # ※本番で試すときは以下をコメントアウト
            self.tap_anywhere(driver, 0.491, 0.340)
            self.tap_button(driver, self.SELECT_BUTTON)
            self.save_screenshot_with_date(driver, "order_complete_410.png")


        except Exception as e:
            print("エラー内容:", e)