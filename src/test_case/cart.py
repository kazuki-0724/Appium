from common.common_const import WaitTime
from common.common_command import CommonCommand
import time
from common.common_const import Direction

class Cart(CommonCommand):

    CALC_IF = "calc_if_button"
    CALC_IF_CLEAR = "calc_order_no_clear_all"
    CALC_IF_ADD = "add"
    CALC_IF_AMOUNT = "amount"
    CALC_IF_ITEM_NO = "itemNo"
    CALC_IF_BUTTON_CHANGE = "button_change"
    CALC_IF_CLOSE = "close"
    ORDER_CONFIRM = "button_order_confirm"
    CLOSE_BTN_IN_MODAL = "toCloseImageView"
    CONFIRM_CHECKBOX = "confirm_checkbox_text"


    def do_test(self,driver):
        try:
            self.test_167_177(self, driver)
            self.test_178_195(self, driver)
            self.test_196_244(self, driver)
            self.test_245_266(self, driver)
            self.test_267_289(self, driver)
            self.test_290_320(self, driver)
            self.test_321_334(self, driver)
            self.test_335_338(self, driver)
            self.test_359_374(self, driver)


        except Exception as e:
            print("エラー内容:", e)

    

    def test_167_177(self, driver):
        try:
            #【注文内容変更】
            # 「カゴ」をタップする
            self.tap_button(driver, self.TAB_CART)
            self.save_screenshot_with_date(driver, "cart_168.png")
            # 画面を最上部に
            self.swipe_vertical(driver, 800, Direction.DOWN.value, WaitTime.SHORT.value)
            self.swipe_vertical(driver, 800, Direction.DOWN.value, WaitTime.SHORT.value)
            self.swipe_vertical(driver, 800, Direction.DOWN.value, WaitTime.SHORT.value)
            
            # ※カゴに「注文商品」しかない状態
            # 「削除」をタップする
            self.long_tap(driver, 0.789, 0.435, 200)
            self.save_screenshot_with_date(driver, "cart_171.png")

            # 「削除をキャンセル」をタップする
            self.long_tap(driver, 0.508, 0.393, 200)
            self.save_screenshot_with_date(driver, "cart_174.png")

            # 数量を変更する
            # 数量欄をタップする
            self.long_tap(driver, 0.9, 0.436, 200)
            # キーボードの「5」をタップする
            self.tap_anywhere(driver, 0.377, 0.783)
            # キーボード領域外をタップで入力を確定させる
            self.long_tap(driver, 0.9, 0.391, 200)
            self.save_screenshot_with_date(driver, "cart_177.png")
        
        except Exception as e:
            print("エラー内容:", e)
    


    def test_178_195(self, driver):
        try:
            
            # 【お届け先確認・変更】
            # 「お届け先を変更する」をタップする
            # self.long_tap(driver, 0.9, 0.391, 200)
            # self.save_screenshot_with_date(driver, "cart_178.png")
            
            # # 一時フレームを閉じる
            # self.tap_button(driver, self.HEADER_CLOSE)
            # self.save_screenshot_with_date(driver, "cart_179.png")
            
            # # 「お届け先を変更する」をタップする
            # self.long_tap(driver, 0.9, 0.391, 200)
            # self.save_screenshot_with_date(driver, "cart_181.png")
            
            # # 「お届け先を追加する」タップする
            # self.long_tap(driver, 0.9, 0.391, 200)
            # self.save_screenshot_with_date(driver, "cart_182.png")

            # # 「変更内容を確定する」タップする
            # self.long_tap(driver, 0.9, 0.391, 200)
            # self.save_screenshot_with_date(driver, "cart_182.png")



            # 【お気に入り商品】


            # 【お買い忘れはありませんか】


            #【お買い忘れはありませんか】
            # ページ最下部まで移動させる
            self.swipe_vertical(driver, 800, Direction.UP.value, WaitTime.SHORT.value)
            self.swipe_vertical(driver, 800, Direction.UP.value, WaitTime.SHORT.value)
            #「いっしょお得対象」をタップする
            self.long_tap(driver, 0.691, 0.742, 200)
            self.save_screenshot_with_date(driver, "cart_194.png")
            self.tap_button(driver, self.HEADER_CLOSE)
            self.save_screenshot_with_date(driver, "cart_195.png")

        except Exception as e:
            print("エラー内容:", e)
    


    def test_196_244(self, driver):
        try:
            #【電卓並び】
            self.tap_button(driver, self.CALC_IF)
            self.tap_button(driver, self.CALC_IF_CLEAR)
            self.save_screenshot_with_date(driver, "cart_196.png")
            
            # 「1」を入力する
            self.tap_button(driver, "button1")
            self.save_screenshot_with_date(driver, "cart_198.png")
            
            # 「11」を入力する
            self.tap_button(driver, "button1")
            self.save_screenshot_with_date(driver, "cart_199.png")

            # 「111」を入力する
            self.tap_button(driver, "button1")
            self.save_screenshot_with_date(driver, "cart_201.png")

            # 商品画像をタップ
            self.long_tap(driver, 0.118, 0.599, 200)
            self.save_screenshot_with_date(driver, "cart_203.png")
            
            # 商品詳細を閉じる
            self.tap_button(driver, self.HEADER_CLOSE)
            self.save_screenshot_with_date(driver, "cart_207.png")

            # 商品名をタップ
            self.long_tap(driver, 0.328, 0.587, 200)
            self.save_screenshot_with_date(driver, "cart_209.png")

            # 商品詳細を閉じる
            self.tap_button(driver, self.HEADER_CLOSE)
            self.save_screenshot_with_date(driver, "cart_213.png")

            # クチコミをタップ
            self.long_tap(driver, 0.275, 0.62, 200)
            self.save_screenshot_with_date(driver, "cart_214.png")



            # 216-228が謎





            # クチコミを閉じる（228次第）
            self.tap_button(driver, self.HEADER_CLOSE)
            self.tap_button(driver, self.CALC_IF_CLEAR)

            # 「1905」を入力する
            self.tap_button(driver, "button1")
            self.tap_button(driver, "button9")
            self.tap_button(driver, "button0")
            self.tap_button(driver, "button5")
            self.save_screenshot_with_date(driver, "cart_229.png")

            # 「19054」を入力する
            self.tap_button(driver, "button4")
            self.save_screenshot_with_date(driver, "cart_230.png")

            # 「190543」を入力する
            self.tap_button(driver, "button3")
            self.save_screenshot_with_date(driver, "cart_231.png")

            # 注文番号入力欄の「x」をタップ
            self.tap_button(driver, self.CALC_IF_CLEAR)
            self.save_screenshot_with_date(driver, "cart_234.png")


            # 「カゴへ」をタップ
            self.tap_button(driver, self.CALC_IF_ADD)
            self.save_screenshot_with_date(driver, "cart_235.png")

            # モーダルを閉じる
            self.tap_anywhere(driver, 0.5, 0.572)
            self.save_screenshot_with_date(driver, "cart_236.png")

            # 数量を入力せずに追加
            self.tap_button(driver, "button1")
            self.tap_button(driver, "button1")
            self.tap_button(driver, "button1")
            # 「数量」をタップ
            self.tap_button(driver, self.CALC_IF_AMOUNT)
            self.tap_button(driver, self.CALC_IF_ADD)
            self.save_screenshot_with_date(driver, "cart_237.png")

            # モーダルを閉じる
            self.tap_anywhere(driver, 0.5, 0.572)
            self.save_screenshot_with_date(driver, "cart_239.png")

            # 「444444」を入力する
            self.tap_button(driver, self.CALC_IF_ITEM_NO)
            self.tap_button(driver, self.CALC_IF_CLEAR)
            self.tap_button(driver, "button4")
            self.tap_button(driver, "button4")
            self.tap_button(driver, "button4")
            self.tap_button(driver, "button4")
            self.tap_button(driver, "button4")
            self.tap_button(driver, "button4")
            self.save_screenshot_with_date(driver, "cart_241.png")

            # 「カゴへ」をタップ
            self.tap_button(driver, self.CALC_IF_ADD)
            self.save_screenshot_with_date(driver, "cart_242.png")

            # モーダルを閉じる
            self.tap_anywhere(driver, 0.5, 0.572)
            self.save_screenshot_with_date(driver, "cart_244.png")

        except Exception as e:
            print("エラー内容:", e)

    

    def test_245_266(self, driver):
        try:
            # 【まとめて買い物セット】
            # 注文番号「113808」を入力する
            self.tap_button(driver, self.CALC_IF_ITEM_NO)
            self.tap_button(driver, "button1")
            self.tap_button(driver, "button1")
            self.tap_button(driver, "button3")
            self.tap_button(driver, "button8")
            self.tap_button(driver, "button0")
            self.tap_button(driver, "button8")
            self.save_screenshot_with_date(driver, "cart_245.png")

            # 商品画像をタップ
            self.long_tap(driver, 0.118, 0.599, 200)
            self.save_screenshot_with_date(driver, "cart_247.png")

            # 「x」ボタンをタップする
            self.tap_button(driver, self.HEADER_CLOSE)
            self.save_screenshot_with_date(driver, "cart_251.png")

            # 商品名をタップ
            self.long_tap(driver, 0.328, 0.587, 200)
            self.save_screenshot_with_date(driver, "cart_253.png")
            
            # 「x」ボタンをタップする
            self.tap_button(driver, self.HEADER_CLOSE)
            self.save_screenshot_with_date(driver, "cart_257.png")

            # クチコミをタップ
            self.long_tap(driver, 0.275, 0.62, 200)
            self.save_screenshot_with_date(driver, "cart_259.png")

            # 「x」ボタンをタップする
            self.tap_button(driver, self.HEADER_CLOSE)
            self.save_screenshot_with_date(driver, "cart_263.png")

            # 「カゴへ」をタップしてエラーモーダルが表示される
            self.tap_button(driver, self.CALC_IF_ADD)
            self.save_screenshot_with_date(driver, "cart_264.png")

            # モーダルを閉じる
            self.tap_anywhere(driver, 0.5, 0.572)
            self.save_screenshot_with_date(driver, "cart_266.png")

        except Exception as e:
            print("エラー内容:", e)

    

    def test_267_289(self, driver):
        try:
            # 【パルくる便】
            # 注文番号「080811」を入力する
            self.tap_button(driver, self.CALC_IF_ITEM_NO)
            self.tap_button(driver, "button0")
            self.tap_button(driver, "button8")
            self.tap_button(driver, "button0")
            self.tap_button(driver, "button8")
            self.tap_button(driver, "button1")
            self.tap_button(driver, "button1")
            self.save_screenshot_with_date(driver, "cart_267.png")

            # 「カゴへ」をタップしてエラーモーダルが表示される
            self.tap_button(driver, self.CALC_IF_ADD)
            self.save_screenshot_with_date(driver, "cart_268.png")

            # モーダルのリンクをタップする
            self.long_tap(driver, 0.684, 0.503, 200)
            self.save_screenshot_with_date(driver, "cart_269.png")

            # かごタブをタップする
            self.tap_button(driver, self.TAB_CART)
            self.save_screenshot_with_date(driver, "cart_272.png")




            # 【特定生協】
            # 注文番号「685」を入力して、「カゴへ」をタップしてエラーモーダルが表示される
            self.tap_button(driver, self.CALC_IF_ITEM_NO)
            self.tap_button(driver, "button6")
            self.tap_button(driver, "button8")
            self.tap_button(driver, "button5")
            self.tap_button(driver, self.CALC_IF_ADD)
            self.save_screenshot_with_date(driver, "cart_273.png")

            # 「詳細はこちら」をタップする
            self.long_tap(driver, 0.498, 0.538, 200)
            self.save_screenshot_with_date(driver, "cart_274.png")

            # かごタブをタップする
            self.tap_button(driver, self.HEADER_CLOSE)
            self.save_screenshot_with_date(driver, "cart_275.png")

            # 「OK」をタップしてエラーモーダルを閉じる
            self.long_tap(driver, 0.5, 0.614, 200)
            self.save_screenshot_with_date(driver, "cart_277.png")




            # 【配列】
            # 「配列」をタップする
            self.tap_button(driver, self.CALC_IF_BUTTON_CHANGE)
            self.save_screenshot_with_date(driver, "cart_279.png")

            # 数字ボタンをタップする
            # self.tap_button(driver, self.CALC_IF_CLEAR)
            self.tap_button(driver, "button0")
            self.tap_button(driver, "button7")
            self.tap_button(driver, "button8")
            self.tap_button(driver, "button9")
            self.tap_button(driver, "button4")
            self.tap_button(driver, "button5")
            self.tap_button(driver, "button6")
            self.save_screenshot_with_date(driver, "cart_280.png")

            # 「配列」をタップする
            self.tap_button(driver, self.CALC_IF_BUTTON_CHANGE)
            self.save_screenshot_with_date(driver, "cart_282.png")

            # 数字ボタンをタップする
            self.tap_button(driver, self.CALC_IF_CLEAR)
            self.tap_button(driver, "button0")
            self.tap_button(driver, "button1")
            self.tap_button(driver, "button2")
            self.tap_button(driver, "button3")
            self.tap_button(driver, "button4")
            self.tap_button(driver, "button5")
            self.tap_button(driver, "button6")
            self.save_screenshot_with_date(driver, "cart_283.png")

            # 「222」を入力する
            self.tap_button(driver, self.CALC_IF_CLEAR)
            self.tap_button(driver, "button2")
            self.tap_button(driver, "button2")
            self.tap_button(driver, "button2")
            self.save_screenshot_with_date(driver, "cart_284.png")

            # 閉じるボタンをタップする
            self.tap_button(driver, self.CALC_IF_CLOSE)
            self.save_screenshot_with_date(driver, "cart_286.png")

            # 電卓IFボタンをタップする
            self.tap_button(driver, self.CALC_IF)
            self.save_screenshot_with_date(driver, "cart_289.png")

        except Exception as e:
            print("エラー内容:", e)
    


    def test_290_320(self, driver):
        try:
            # 【商品詳細画面】
            # 「111」の商品画像をタップ
            self.long_tap(driver, 0.121, 0.364, 200)
            self.save_screenshot_with_date(driver, "cart_291.png")

            self.scroll_vertical(driver, 256, Direction.DOWN.value)
            # 商品情報の「？」をタップする
            self.long_tap(driver, 0.522, 0.818, 200)
            self.save_screenshot_with_date(driver, "cart_292.png")

            # 「←」をタップする
            self.tap_button(driver, self.BACK)
            self.save_screenshot_with_date(driver, "cart_293.png")
          
            # 「クチコミ」をタップする
            self.tap_anywhere(driver, 0.395, 0.818)
            self.save_screenshot_with_date(driver, "cart_294.png")

            # 「x」をタップする
            self.tap_button(driver, self.HEADER_CLOSE)
            self.save_screenshot_with_date(driver, "cart_296.png")

            # 「111」の商品画像をタップ
            self.long_tap(driver, 0.366, 0.356, 200)
            self.save_screenshot_with_date(driver, "cart_297.png")

            # お気に入りが見えるまでスクロール
            self.scroll_vertical(driver, 487, Direction.DOWN.value)
            # お気に入りをタップする
            self.long_tap(driver, 0.310, 0.842, 200)
            self.save_screenshot_with_date(driver, "cart_298.png")

            # 「x」をタップする
            self.tap_button(driver, self.HEADER_CLOSE)
            self.save_screenshot_with_date(driver, "cart_299.png")


            # 「111」の商品画像をタップ
            self.long_tap(driver, 0.366, 0.356, 200)
            self.save_screenshot_with_date(driver, "cart_302.png")

            # お気に入りが見えるまでスクロール
            self.scroll_vertical(driver, 445, Direction.DOWN.value)
            # お気に入りをタップする
            self.long_tap(driver, 0.310, 0.858, 200)
            self.save_screenshot_with_date(driver, "cart_303.png")

            # 「x」をタップする
            self.tap_button(driver, self.HEADER_CLOSE)
            self.save_screenshot_with_date(driver, "cart_306.png")


            # 「111」の商品名をタップ
            self.long_tap(driver, 0.366, 0.356, 200)
            self.save_screenshot_with_date(driver, "cart_307.png")

            # 「カゴへ」をタップする
            self.tap_anywhere(driver, 0.869, 0.945)
            self.save_screenshot_with_date(driver, "cart_308.png")

            # 「x」をタップする
            self.tap_button(driver, self.HEADER_CLOSE)
            self.save_screenshot_with_date(driver, "cart_313.png")

            # 「111」の商品名をタップ
            self.long_tap(driver, 0.366, 0.356, 200)
            self.save_screenshot_with_date(driver, "cart_314.png") 

            # 「削除」をタップする
            self.tap_anywhere(driver, 0.673, 0.944)
            self.save_screenshot_with_date(driver, "cart_315.png")

            # 「x」をタップする
            self.tap_button(driver, self.HEADER_CLOSE)
            self.save_screenshot_with_date(driver, "cart_320.png")

        except Exception as e:
            print("エラー内容:", e)

    

    def test_321_334(self, driver):
        try:
            # 【画面制御】
            # 一番下までスクロール
            self.scroll_vertical(driver, 800, Direction.DOWN.value)
            self.scroll_vertical(driver, 800, Direction.DOWN.value)
            self.scroll_vertical(driver, 800, Direction.DOWN.value)
            self.save_screenshot_with_date(driver, "cart_321-1.png")

            self.tap_button(driver, self.TAB_CART)
            self.save_screenshot_with_date(driver, "cart_321-2.png")

            # 322-334はやり方考える


        except Exception as e:
            print("エラー内容:", e)



    def test_335_338(self, driver):
        try:
            #【レコメンドモーダル】
            self.tap_button(driver, self.TAB_CART)
            # 「注文へ進む」をタップする
            self.tap_button(driver, self.ORDER_CONFIRM)
            self.save_screenshot_with_date(driver, "cart_336.png")

            # 「追加」をタップする
            self.tap_anywhere(driver, 0.838, 0.306)
            self.save_screenshot_with_date(driver, "cart_337.png")

            # モーダルの「x」をタップする
            self.tap_button(driver, self.CLOSE_BTN_IN_MODAL)
            self.save_screenshot_with_date(driver, "cart_342.png")

            # 「注文へ進む」をタップする
            self.tap_button(driver, self.ORDER_CONFIRM)
            self.save_screenshot_with_date(driver, "cart_343.png")

            # 商品画像をタップする
            self.tap_anywhere(driver, 0.135, 0.279)
            self.save_screenshot_with_date(driver, "cart_345.png")

            # 「x」をタップする
            self.tap_button(driver, self.HEADER_CLOSE)
            self.save_screenshot_with_date(driver, "cart_346.png")

            # モーダルの「x」をタップする
            self.tap_button(driver, self.CLOSE_BTN_IN_MODAL)
            self.save_screenshot_with_date(driver, "cart_348.png")

            # 「注文へ進む」をタップする
            self.tap_button(driver, self.ORDER_CONFIRM)
            self.save_screenshot_with_date(driver, "cart_349.png")

            # 商品名をタップする
            self.tap_anywhere(driver, 0.296, 0.269)
            self.save_screenshot_with_date(driver, "cart_350.png")

            # 「カゴへ」をタップする
            self.tap_anywhere(driver, 0.869, 0.945)
            self.save_screenshot_with_date(driver, "cart_351.png")

            # 「x」をタップする
            self.tap_button(driver, self.HEADER_CLOSE)
            self.save_screenshot_with_date(driver, "cart_353.png")

            # 「この企画回で再表示しない」
            self.tap_button(driver, self.CONFIRM_CHECKBOX)


            # 354-358

        except Exception as e:
            print("エラー内容:", e)



    def test_359_374(self, driver):
        try:
            # 【注文チェック】
            print("")

        
        except Exception as e:
            print("エラー内容:", e)   