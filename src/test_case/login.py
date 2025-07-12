from common.common_const import WaitTime
from common.common_command import CommonCommand

class Login(CommonCommand):

    # パーツID
    ID = "authIdEditText"
    PASSWORD = "passwordEditText"
    LOGIN_BUTTON = "loginBtn"
    HELP = "forgetAuthInfoTextView"
    GO_LOGIN = "goto_login_btn"
    
    def do_test(self,driver):
        try:
            # ログイン画面
            self.tap_button(driver, Login.GO_LOGIN, WaitTime.SHORT.value)
            self.save_screenshot_with_date(driver, "login_038.png")
            self.tap_anywhere(driver, 0.507, 0.207)
            self.save_screenshot_with_date(driver, "login_040.png")

            self.input_text(driver, Login.ID, "hogehoge", WaitTime.SHORT.value)
            self.tap_anywhere(driver, 0.507, 0.283)
            self.save_screenshot_with_date(driver, "login_042.png")

            self.input_text(driver, Login.PASSWORD, "password", WaitTime.SHORT.value)
            self.save_screenshot_with_date(driver, "login_043.png")

            self.tap_button(driver, Login.HELP, WaitTime.SHORT.value)
            self.save_screenshot_with_date(driver, "login_045.png")
            
            self.tap_anywhere(driver, 0.216, 0.346)
            self.save_screenshot_with_date(driver, "login_046.png")
            self.tap_back_button(driver, WaitTime.SHORT.value)
            self.save_screenshot_with_date(driver, "login_047.png")
            self.tap_anywhere(driver, 0.216, 0.468)
            self.save_screenshot_with_date(driver, "login_048.png")
            self.tap_back_button(driver, WaitTime.SHORT.value)
            self.save_screenshot_with_date(driver, "login_049.png")
            self.tap_back_button(driver, WaitTime.SHORT.value)

            self.input_text(driver, Login.ID, "9m10411", WaitTime.SHORT.value)
            self.input_text(driver, Login.PASSWORD, "pal000", WaitTime.SHORT.value)
            # self.input_text(driver, Login.ID, "7500007", WaitTime.SHORT.value)
            # self.input_text(driver, Login.PASSWORD, "000000", WaitTime.SHORT.value)
            self.tap_button(driver, Login.LOGIN_BUTTON, WaitTime.SHORT.value)

        except Exception as e:
            print("エラー内容:", e)