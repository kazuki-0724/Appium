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
            self.save_screenshot_with_date(driver, "item_search_139.png")

            # キャンセルボタンをタップ
            self.tap_button(driver, ItemSearch.CANCEL)
            self.save_screenshot_with_date(driver, "item_search_140.png")

            # 「検索」をタップする
            self.tap_button(driver, self.HEADER_SEARCH)
            self.save_screenshot_with_date(driver, "item_search_141.png")

            # 入力欄をタップ
            self.tap_anywhere(driver, 0.472, 0.078)
            self.input_text(driver, ItemSearch.SEARCH_EDIT_TEXT, "")
            # 空入力で検索実行
            driver.press_keycode(66)
            self.save_screenshot_with_date(driver, "item_search_142.png")

            # 「OK」をタップ
            self.tap_anywhere(driver, 0.5, 0.592)
            self.save_screenshot_with_date(driver, "item_search_143.png")

            # 入力欄をタップ
            self.tap_anywhere(driver, 0.472, 0.078)
            # 「果汁100%」を入力して検索
            self.input_text(driver, ItemSearch.SEARCH_EDIT_TEXT, "果汁100%")
            driver.press_keycode(66)
            self.save_screenshot_with_date(driver, "item_search_146.png")

            # 「検索」をタップ
            self.tap_button(driver, self.HEADER_SEARCH)
            self.save_screenshot_with_date(driver, "item_search_147.png")

            # 「たま」を入力
            self.input_text(driver, ItemSearch.SEARCH_EDIT_TEXT, "たま")
            self.save_screenshot_with_date(driver, "item_search_148.png")

            # 「産直たまご」をタップする
            self.tap_anywhere(driver, 0.142, 0.128)
            self.save_screenshot_with_date(driver, "item_search_150.png")
            
            # 「検索」をタップ
            self.tap_button(driver, self.HEADER_SEARCH)
            self.save_screenshot_with_date(driver, "item_search_151.png")

            # 「たま」を入力
            self.input_text(driver, ItemSearch.SEARCH_EDIT_TEXT, "たま")
            self.save_screenshot_with_date(driver, "item_search_152.png")

            # 「玉ねぎ　2個」をタップする
            self.tap_anywhere(driver, 0.142, 0.128)
            self.save_screenshot_with_date(driver, "item_search_154.png")

            # 「検索」をタップ
            self.tap_button(driver, self.HEADER_SEARCH)
            self.save_screenshot_with_date(driver, "item_search_156.png")

            # 履歴の一番下「果汁100%」をタップ
            self.tap_anywhere(driver, 0.142, 0.232)
            self.save_screenshot_with_date(driver, "item_search_158.png")

            # キャンセルボタンをタップ
            self.tap_button(driver, ItemSearch.CANCEL)

            # 「あいうえおかきくけこ」の順で検索する
            self.tap_button(driver, self.HEADER_SEARCH)
            self.input_text(driver, ItemSearch.SEARCH_EDIT_TEXT, "あ")
            driver.press_keycode(66)

            self.tap_button(driver, self.HEADER_SEARCH)
            self.input_text(driver, ItemSearch.SEARCH_EDIT_TEXT, "い")
            driver.press_keycode(66)
            
            self.tap_button(driver, self.HEADER_SEARCH)
            self.input_text(driver, ItemSearch.SEARCH_EDIT_TEXT, "う")
            driver.press_keycode(66)

            self.tap_button(driver, self.HEADER_SEARCH)
            self.input_text(driver, ItemSearch.SEARCH_EDIT_TEXT, "え")
            driver.press_keycode(66)

            self.tap_button(driver, self.HEADER_SEARCH)
            self.input_text(driver, ItemSearch.SEARCH_EDIT_TEXT, "お")
            driver.press_keycode(66)

            self.tap_button(driver, self.HEADER_SEARCH)
            self.input_text(driver, ItemSearch.SEARCH_EDIT_TEXT, "か")
            driver.press_keycode(66)

            self.tap_button(driver, self.HEADER_SEARCH)
            self.input_text(driver, ItemSearch.SEARCH_EDIT_TEXT, "き")
            driver.press_keycode(66)
            
            self.tap_button(driver, self.HEADER_SEARCH)
            self.input_text(driver, ItemSearch.SEARCH_EDIT_TEXT, "く")
            driver.press_keycode(66)
            
            self.tap_button(driver, self.HEADER_SEARCH)
            self.input_text(driver, ItemSearch.SEARCH_EDIT_TEXT, "け")
            driver.press_keycode(66)
            
            self.tap_button(driver, self.HEADER_SEARCH)
            self.input_text(driver, ItemSearch.SEARCH_EDIT_TEXT, "こ")
            driver.press_keycode(66)

            # 「検索」をタップする
            self.tap_button(driver, self.HEADER_SEARCH)
            self.save_screenshot_with_date(driver, "item_search_160.png")

            # 「たまご」を入力して、検索を実行
            self.input_text(driver, ItemSearch.SEARCH_EDIT_TEXT, "たまご")
            driver.press_keycode(66)
            self.save_screenshot_with_date(driver, "item_search_161.png")

            # 「検索」をタップする
            self.tap_button(driver, self.HEADER_SEARCH)
            self.save_screenshot_with_date(driver, "item_search_164.png")

            # 「い」を削除する
            self.tap_anywhere(driver, 0.957, 0.578)
            self.save_screenshot_with_date(driver, "item_search_165.png")
            
            # キャンセルボタンをタップ
            self.tap_button(driver, ItemSearch.CANCEL)
            self.save_screenshot_with_date(driver, "item_search_166.png")

        except Exception as e:
            print("エラー内容:", e)