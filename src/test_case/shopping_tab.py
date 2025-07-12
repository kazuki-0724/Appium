from common.common_const import WaitTime
from common.common_command import CommonCommand
from common.common_const import Direction

class ShoppingTab(CommonCommand):

    # パーツID
    ORDER_CONFIRM = "button_order_confirm"
    ORDER_CONFIRM_IN_REC_MODAL = "toPurchaseText"
    ORDER_COMPLETE = "button_order_complete"
    CONTINUE_SHOPPING = "button_continue_shopping"
    PROCATALOG_SELECT = "productCatalogSelectBtn"

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


    def do_sample_test(self, driver):
        try:
            # カゴを空にする(商品のタップエリアを確定させるため)
            self.clear_cart(driver)
            
            # 赤バッチを消すために一度注文送信を行う
            self.tap_button(driver, self.TAB_CART)
            self.tap_button(driver, self.ORDER_CONFIRM)
            self.tap_button(driver, self.ORDER_CONFIRM_IN_REC_MODAL)
            self.tap_button(driver, self.ORDER_COMPLETE)
            self.tap_button(driver, self.CONTINUE_SHOPPING)
            self.tap_button(driver, self.PROCATALOG_SELECT)
            # 赤バッチが消えていることの確認
            self.save_screenshot_with_date(driver, "shopping_tab_98.png")

            # 任意の商品を追加する
            self.long_tap(driver, 0.870, 0.877, 200)
            self.save_screenshot_with_date(driver, "shopping_tab_100.png")

            # カゴタブをタップ
            self.tap_button(driver, self.TAB_CART)
            self.save_screenshot_with_date(driver, "shopping_tab_103.png",0)

            # さっき追加した商品を数量変更
            # 数量欄をタップする
            self.long_tap(driver, 0.9, 0.436, 200)
            # キーボードの「5」をタップする
            540,1738
            self.tap_anywhere(driver, 0.500, 0.720)
            # キーボード領域外をタップで入力を確定させる
            self.long_tap(driver, 0.9, 0.165, 200)
            self.save_screenshot_with_date(driver, "shopping_tab_104.png")
            

            # 「買い物」タブをタップ
            self.tap_button(driver, self.TAB_SHOPPING)
            
            # TODO: 買い物タブタブで追加した商品の場所までスクロールさせる
            self.scroll_vertical(driver, 1921, Direction.DOWN.value, WaitTime.SHORT.value)
            self.save_screenshot_with_date(driver, "shopping_tab_106.png")
            

            self.scroll_vertical(driver, 1921, Direction.DOWN.value, WaitTime.SHORT.value)
            self.scroll_vertical(driver, 1954, Direction.DOWN.value, WaitTime.SHORT.value)
            self.scroll_vertical(driver, 1702, Direction.DOWN.value, WaitTime.SHORT.value)

            # 「【view=pochiなし】同窓遷移」をタップ
            self.long_tap(driver, 0.157, 0.345, 200)

            self.save_screenshot_with_date(driver, "shopping_tab_108.png")
                    
        except Exception as e:
            print("エラー内容:", e)