from common.common_const import WaitTime
from common.common_command import CommonCommand
import time

class Splash(CommonCommand):
    
    def do_test(self,driver):
        try:
            # スプラッシュ画面
            time.sleep(1)
            self.save_screenshot_with_date(driver, "splash_005.png")
            time.sleep(30)
            
        except Exception as e:
            print("エラー内容:", e)