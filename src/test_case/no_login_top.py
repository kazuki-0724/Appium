from common.common_const import WaitTime
from common.common_command import CommonCommand


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
            self.tap_button(driver, NoLoginTop.LEFT, WaitTime.SHORT.value)
            self.save_screenshot_with_date(driver, "no_login_top_010.png")
            self.tap_button(driver, NoLoginTop.RIGHT, WaitTime.SHORT.value)
            self.save_screenshot_with_date(driver, "no_login_top_012.png")
            self.tap_button(driver, NoLoginTop.RIGHT, WaitTime.SHORT.value)
            self.save_screenshot_with_date(driver, "no_login_top_016.png")
            self.tap_button(driver, NoLoginTop.LEFT, WaitTime.SHORT.value)
            self.tap_button(driver, NoLoginTop.LEFT, WaitTime.SHORT.value)
            self.save_screenshot_with_date(driver, "no_login_top_021.png")

        except Exception as e:
            print("エラー内容:", e)