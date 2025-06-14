from common.common_const import WaitTime
from common.common_command import CommonCommand
import time

class OrderConfirm(CommonCommand):

    ORDER_CONFIRM = "button_order_confirm"
    
    def do_test(self,driver):
        try:
            # 注文内容確認
            self.tap_button(driver, self.TAB_CART)
            self.tap_button(driver, self.ORDER_CONFIRM)
            
        except Exception as e:
            print("エラー内容:", e)