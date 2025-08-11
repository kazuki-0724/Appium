from common.common_const import WaitTime
from common.common_command import CommonCommand
import time

class PalPromo(CommonCommand):

    # パーツID
    REGISTER_BTN_IN_ITEM = "registerBtn3"
    REGISTER_BTN_IN_MODAL = "dialogOkBtn"
    FOOTER_BTN = "parukuluBtn"
    
    def do_test(self,driver):
        try:
            # パルくる便プロモーション            
            time.sleep(2)
            # 表示確認
            self.save_screenshot_with_date(driver, "pal_promo_130.png")
            
            # # 「登録する」をタップ
            # self.tap_button(driver, self.REGISTER_BTN_IN_ITEM, WaitTime.SHORT.value)
            self.tap_anywhere(driver, 0.889, 0.737)
            self.save_screenshot_with_date(driver, "pal_promo_132.png")

            # # モーダルの「登録する」をタップ
            self.tap_button(driver, self.REGISTER_BTN_IN_MODAL, WaitTime.SHORT.value)
            self.save_screenshot_with_date(driver, "pal_promo_134.png")

            # 「対象商品一覧・登録管理」をタップ
            self.tap_button(driver, self.FOOTER_BTN, WaitTime.SHORT.value)
            self.sleep(WaitTime.LONG.value)
            self.save_screenshot_with_date(driver, "pal_promo_136.png")

            # 買い物タブをタップ
            self.tap_button(driver, self.TAB_SHOPPING, WaitTime.SHORT.value)
            self.save_screenshot_with_date(driver, "pal_promo_137.png")
            
        except Exception as e:
            print("エラー内容:", e)