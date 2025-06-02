from common.common_const import WaitTime
from common.common_command import CommonCommand
from common.common_const import Direction

class ShoppingTab(CommonCommand):

    # パーツID

    def do_test(self,driver):
        try:
            # 買い物タブ
            self.tap_button(driver, self.HEADER_CATALOG, WaitTime.SHORT.value)
            # 左上のカタログをタップ（座標は端末により調整）
            self.tap_anywhere(driver, 293, 737)

            # 使い方
            # 「次に進む」をタップ
            self.tap_anywhere(driver, 814, 1754)
            # 「次に進む」をタップ
            self.tap_anywhere(driver, 814, 1754)
            # 「次に進む」をタップ
            self.tap_anywhere(driver, 814, 1754)
            # 「はじめる」をタップ
            self.tap_anywhere(driver, 814, 1754)

            #「＞」タップ
            self.tap_anywhere(driver, 976, 2104)
            self.sleep(WaitTime.SHORT.value)
            self.check_element_text(driver, self.HEADER_FEE_TOTAL)
            # 商品タップ（追加）
            #self.tap_anywhere(driver, 148, 1058)
            self.long_tap(driver, 148, 1058)
            self.tap_anywhere(driver, 896, 1299)
            self.tap_anywhere(driver, 1019, 974)
            self.sleep(WaitTime.SHORT.value)
            self.check_element_text(driver, self.HEADER_FEE_TOTAL)

            # 商品タップ（商品モーダル）
            self.tap_anywhere(driver, 148, 1058)
            self.tap_anywhere(driver, 1019, 974)
            self.tap_back_button(driver, WaitTime.SHORT.value)

            # カテゴリ画面
            self.tap_button(driver, self.HEADER_CATEGORY, WaitTime.SHORT.value)
            self.swipe_vertical(driver, 800, Direction.UP.value, WaitTime.SHORT.value)
            self.swipe_vertical(driver, 800, Direction.UP.value, WaitTime.SHORT.value)

            self.tap_button(driver, self.TAB_SHOPPING, WaitTime.SHORT.value)


        except Exception as e:
            print("エラー内容:", e)