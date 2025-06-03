from common.common_const import WaitTime
from common.common_command import CommonCommand
from common.common_const import Direction

class ShoppingTab(CommonCommand):

    # パーツID

    def do_test(self,driver):
        try:
            # 買い物タブ
            self.tap_button(driver, self.HEADER_CATALOG)
            self.save_screenshot_with_date(driver, "shopping_tab_062.png")

            # 左上のカタログをタップ（座標は端末により調整）
            self.tap_anywhere(driver, 0.250, 0.309)
            
            # 使い方が表示される場合
            # 「次に進む」をタップ
            self.tap_anywhere(driver, 0.748, 0.729)
            # 「次に進む」をタップ
            self.tap_anywhere(driver, 0.748, 0.729)
            # 「次に進む」をタップ
            self.tap_anywhere(driver, 0.748, 0.729)
            # 「はじめる」をタップ
            self.tap_anywhere(driver, 0.748, 0.729)
            self.save_screenshot_with_date(driver, "shopping_tab_066.png")

            # カタログの「＞」をタップ（次ページに移動）
            self.tap_anywhere(driver, 0.908, 0.871)
            self.sleep(WaitTime.SHORT.value)
            self.check_element_text(driver, self.HEADER_FEE_TOTAL)

            # 商品タップ（追加）
            self.long_tap(driver, 0.131, 0.406, 400)
            # 「カゴへ」をタップ
            self.long_tap(driver, 0.832, 0.605, 200)
            # # 「商品モーダル「x」」をタップ
            self.long_tap(driver, 0.946, 0.371, 200)
            # ※上記処理について本来は1回タップで追加したい
            self.save_screenshot_with_date(driver, "shopping_tab_070.png")




            # 商品タップ（商品モーダル）
            self.long_tap(driver, 0.131, 0.406, 400)
            self.save_screenshot_with_date(driver, "shopping_tab_071.png")
            # 「商品名」をタップ
            self.long_tap(driver, 0.617, 0.423, 200)
            self.save_screenshot_with_date(driver, "shopping_tab_073.png")
            # 画面ロードさせるために（5秒スリープ）
            self.sleep(WaitTime.LONG.value)
            # OF「x」をタップ
            self.tap_button(driver, self.HEADER_CLOSE)
            self.save_screenshot_with_date(driver, "shopping_tab_075.png")
            # 「商品名」をタップ
            self.long_tap(driver, 0.617, 0.423, 200)
            self.save_screenshot_with_date(driver, "shopping_tab_078.png")
            # WebViewの「カゴへ」をタップ
            self.long_tap(driver, 0.867, 0.946, 200)
            self.save_screenshot_with_date(driver, "shopping_tab_079.png")
            # OF「x」をタップ
            self.tap_button(driver, self.HEADER_CLOSE)
            self.save_screenshot_with_date(driver, "shopping_tab_081.png")
            # 「商品モーダル「x」」をタップ
            self.long_tap(driver, 0.946, 0.371, 200)
            # カタログの「＞」をタップ（次ページに移動）
            self.tap_anywhere(driver, 0.908, 0.871)
            self.save_screenshot_with_date(driver, "shopping_tab_082.png")
            # ヘッダーの「←」をタップ
            self.tap_button(driver, self.BACK)
            self.save_screenshot_with_date(driver, "shopping_tab_083.png")
            # ヘッダーの「←」をタップ
            self.tap_button(driver, self.BACK)
            self.save_screenshot_with_date(driver, "shopping_tab_084.png")

            # カテゴリ画面
            self.tap_button(driver, self.HEADER_CATEGORY, WaitTime.SHORT.value)
            self.save_screenshot_with_date(driver, "shopping_tab_085.png")
            # 1番下までスクロール
            self.swipe_vertical(driver, 800, Direction.UP.value, WaitTime.SHORT.value)
            self.swipe_vertical(driver, 800, Direction.UP.value, WaitTime.SHORT.value)
            self.save_screenshot_with_date(driver, "shopping_tab_086.png")

            # 86,87,88,89が無理


            self.tap_button(driver, self.TAB_CART)
            self.save_screenshot_with_date(driver, "shopping_tab_090.png")

            self.tap_button(driver, self.TAB_SHOPPING)
            self.save_screenshot_with_date(driver, "shopping_tab_091.png")

            self.tap_button(driver, self.TAB_SHOPPING)
            self.save_screenshot_with_date(driver, "shopping_tab_092.png")

            self.tap_button(driver, self.TAB_CART)
            self.save_screenshot_with_date(driver, "shopping_tab_093.png")

            self.tap_button(driver, self.TAB_SHOPPING)
            self.save_screenshot_with_date(driver, "shopping_tab_094.png")


            self.swipe_vertical(driver, 800, Direction.UP.value, WaitTime.SHORT.value)
            self.swipe_vertical(driver, 800, Direction.UP.value, WaitTime.SHORT.value)
            self.save_screenshot_with_date(driver, "shopping_tab_095-1.png")

            self.tap_button(driver, self.TAB_SHOPPING)
            self.save_screenshot_with_date(driver, "shopping_tab_095-2.png")

            # 適当な商品をクリックして商品詳細へ
            self.long_tap(driver, 0.447, 0.494, 200)
            self.save_screenshot_with_date(driver, "shopping_tab_096.png")

            self.tap_button(driver, self.TAB_SHOPPING)
            self.save_screenshot_with_date(driver, "shopping_tab_097.png")

        except Exception as e:
            print("エラー内容:", e)