from common.common_const import WaitTime
from common.common_command import CommonCommand
import time

class ItemSearch(CommonCommand):
    
    CANCEL = "header_right_text"
    SEARCH_EDIT_TEXT = "search_word"

    def do_test(self,driver):
        try:
            # 商品検索画面
            self.tap_button(driver, self.HEADER_SEARCH)
            self.save_screenshot_with_date(driver, "item_search.png")
            # キャンセルボタンをタップ
            self.tap_button(driver, ItemSearch.CANCEL)
            self.tap_button(driver, self.HEADER_SEARCH)

            self.input_text(driver, ItemSearch.SEARCH_EDIT_TEXT, "りんご")


        except Exception as e:
            print("エラー内容:", e)