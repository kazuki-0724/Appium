# ディレクトリ: Appium/src/test_case

---

### ファイル: Appium/src/test_case/account_create.py

```python
from common.common_const import WaitTime
from common.common_command import CommonCommand

class AccountCreate(CommonCommand):

    # パーツID
    ACCOUNT_BUTTON = "goto_creat_account_btn"
    


    def do_test(self,driver):
        try:
            # アカウント設定
            self.tap_button(driver, AccountCreate.ACCOUNT_BUTTON, WaitTime.SHORT.value)
            self.save_screenshot_with_date(driver, "account_create_022.png")
            # 「よくある問い合わせ」
            #self.long_tap(driver, 534, 1915, 300)
            self.long_tap(driver, 0.494, 0.793, 300)
            # ナビゲーションの確認「このページから移動」
            self.long_tap(driver, 0.719, 0.619, 100)
            self.save_screenshot_with_date(driver, "account_create_023.png")
            self.tap_button(driver, self.HEADER_CLOSE, WaitTime.SHORT.value)
            self.save_screenshot_with_date(driver, "account_create_024.png")
            # 組合員番号（WebView）
            self.long_tap(driver, 0.268, 0.399, 100)
            # 組合員番号(8桁)をIMEで入力
            for i in range(8):
                self.long_tap(driver, 0.390, 0.783, 100)
            # 登録済みの電話番号（WebView）
            self.long_tap(driver, 0.282, 0.550, 100)
            # 登録済みの電話番号(11桁)をIMEで入力
            for i in range(11):
                self.long_tap(driver, 0.390, 0.783, 100)
            # IMEを非表示にする
            self.long_tap(driver, 0.841, 0.579, 100)
            # 「電話番号確認用コードを送信する」をタップ
            self.long_tap(driver, 0.374, 0.807, 100)
            # ダイアログ「キャンセル」をタップ（ネイティブのため絶対座標）
            self.long_tap(driver, 0.649, 0.606, 100)
            self.save_screenshot_with_date(driver, "account_create_028.png")
            self.tap_back_button(driver,WaitTime.SHORT.value)


        except Exception as e:
            print("エラー内容:", e)
```

---

### ファイル: Appium/src/test_case/cart.py

```python
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
            # self.test_167_177(driver)
            # self.test_178_195(driver)
            # self.test_196_244(driver)
            # self.test_245_266(driver)
            # self.test_267_289(driver)
            # self.test_290_320(driver)
            # self.test_321_334(driver)
             self.test_335_338(driver)
            # self.test_359_374(driver)


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
            self.long_tap(driver, 0.9, 0.165, 200)
            self.save_screenshot_with_date(driver, "cart_177.png")
        
        except Exception as e:
            print("エラー内容:", e)
    


    def test_178_195(self, driver):
        try:
            
            # カゴを空にする（一番上にお届け先指定の商品を持ってくるため）
            self.clear_cart(driver)
            
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
            self.long_tap(driver, 0.129, 0.689, 200)
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
            self.long_tap(driver, 0.175, 0.595, 200)
            self.save_screenshot_with_date(driver, "cart_218.png")
            
            # クチコミを閉じる
            self.tap_button(driver, self.HEADER_CLOSE)
            self.save_screenshot_with_date(driver, "cart_222.png")
            
            # 「カゴへ」をタップする
            self.tap_button(driver, self.CALC_IF_ADD)
            self.save_screenshot_with_date(driver, "cart_228.png")
            
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
            self.tap_anywhere(driver, 0.5, 0.616)
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
            self.save_screenshot_with_date(driver, "cart_271.png")

            self.tap_anywhere(driver, 0.5, 0.616)
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

            # 「X」をタップする
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
            self.tap_button(driver, self.CALC_IF_CLEAR)
            self.tap_button(driver, "button0")
            self.tap_button(driver, "button7")
            self.tap_button(driver, "button8")
            self.tap_button(driver, "button9")
            self.tap_button(driver, "button4")
            self.tap_button(driver, "button5")
            self.save_screenshot_with_date(driver, "cart_280-1.png")
            self.tap_button(driver, self.CALC_IF_CLEAR)
            self.tap_button(driver, "button6")
            self.tap_button(driver, "button1")
            self.tap_button(driver, "button2")
            self.tap_button(driver, "button3")
            self.save_screenshot_with_date(driver, "cart_280-2.png")


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
            self.save_screenshot_with_date(driver, "cart_283-1.png")
            self.tap_button(driver, "button6")
            self.tap_button(driver, "button7")
            self.tap_button(driver, "button8")
            self.tap_button(driver, "button9")
            self.save_screenshot_with_date(driver, "cart_283-2.png")

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
            self.tap_anywhere(driver, 0.366, 0.721)
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

            # 一度カゴを空にして「101」の商品を一つだけ追加する
            self.clear_cart(driver)
            self.tap_button(driver, self.CALC_IF)
            self.tap_button(driver, "button1")
            self.tap_button(driver, "button0")
            self.tap_button(driver, "button1")
            self.tap_button(driver, self.CALC_IF_ADD)
            
            # 「101」の商品を削除する
            self.tap_anywhere(driver, 0.673, 0.944)
            self.save_screenshot_with_date(driver, "cart_324.png")
            
            # 買い物タブをタップする
            self.tap_button(driver, self.TAB_SHOPPING)
            self.save_screenshot_with_date(driver, "cart_325.png")
            
            # カゴタブをタップする
            self.tap_button(driver, self.TAB_CART)
            self.save_screenshot_with_date(driver, "cart_327.png")
            
            # 「101」の数量欄をタップする
            self.long_tap(driver, 0.9, 0.436, 200)
            # キーボードの「←（削除）」をタップする
            self.tap_anywhere(driver, 0.871, 0.846)
            # キーボード領域外をタップで入力を確定させる
            self.long_tap(driver, 0.9, 0.165, 200)
            self.save_screenshot_with_date(driver, "cart_328.png")
            
            # 注文へ進むをタップする
            self.tap_button(driver, self.ORDER_CONFIRM)
            self.save_screenshot_with_date(driver, "cart_329.png")
            
            # モーダルの「確認」をタップする
            self.tap_anywhere(driver, 0.499, 0.571)
            self.save_screenshot_with_date(driver, "cart_331.png")
            
            # 「101」の数量欄をタップする
            self.long_tap(driver, 0.9, 0.436, 200)
            # キーボードの「1」をタップする
            self.tap_anywhere(driver, 0.122, 0.722)
            # キーボード領域外をタップで入力を確定させる
            self.long_tap(driver, 0.9, 0.165, 200)
            self.save_screenshot_with_date(driver, "cart_334.png")


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
```

---

### ファイル: Appium/src/test_case/item_search.py

```python
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
```

---

### ファイル: Appium/src/test_case/login.py

```python
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
```

---

### ファイル: Appium/src/test_case/must_read_modal.py

```python
from common.common_const import WaitTime
from common.common_command import CommonCommand
import time
from common.common_const import Direction

class MustReadModal(CommonCommand):

    # パーツID
    CONFIRM_CHECKBOX = "confirm_checkbox_text"
    CLOSE_BTN = "closeBtn"
    

    def do_test(self,driver):
        try:
            # 必読モーダル
            time.sleep(2)
            # 上記表示確認
            self.save_screenshot_with_date(driver, "must_read_modal_112.png")
            
            # 下部まで移動
            self.swipe_vertical(driver, 500, Direction.UP.value)
            self.save_screenshot_with_date(driver, "must_read_modal_113.png")

            # チェックボックスをチェック
            self.tap_button(driver, self.CONFIRM_CHECKBOX, WaitTime.SHORT.value)
            self.save_screenshot_with_date(driver, "must_read_modal_117.png")
            
            # 上部まで移動
            self.swipe_vertical(driver, 500, Direction.DOWN.value)
            self.save_screenshot_with_date(driver, "must_read_modal_118.png")

            # 下部まで移動
            self.swipe_vertical(driver, 500, Direction.UP.value)
            self.save_screenshot_with_date(driver, "must_read_modal_119.png")

            # チェックボックスをチェックアウト
            self.tap_button(driver, self.CONFIRM_CHECKBOX, WaitTime.SHORT.value)
            self.save_screenshot_with_date(driver, "must_read_modal_121.png")

            # チェックボックスをチェック
            self.tap_button(driver, self.CONFIRM_CHECKBOX, WaitTime.SHORT.value)
            self.save_screenshot_with_date(driver, "must_read_modal_123.png")

            # 領域外タップ
            self.long_tap(driver, 0.880, 0.963,200)
            self.save_screenshot_with_date(driver, "must_read_modal_124.png")

            # チェックボックスをチェック
            self.tap_button(driver, self.CLOSE_BTN, WaitTime.SHORT.value)
            self.save_screenshot_with_date(driver, "must_read_modal_125.png")
            
        except Exception as e:
            print("エラー内容:", e)
```

---

### ファイル: Appium/src/test_case/no_login_top.py

```python
from common.common_const import WaitTime
from common.common_command import CommonCommand
import time
from datetime import datetime
from common.common_const import Direction

class NoLoginTop(CommonCommand):
    
    # パーツID
    CREATE_ACCOUNT = "goto_creat_account_btn"
    CONTENTS = "contents_imageview"
    LEFT = "back_icon_imageview"
    RIGHT = "forward_icon_imageview"
    GO_LOGIN = "goto_login_btn"
    
    
    def do_test(self,driver):
        try:
            # 未ログイントップ
            self.save_screenshot_with_date(driver, "no_login_top_007.png")

            self.swipe_contents_horizontaly(driver, 250, Direction.RIGHT.value)
            self.save_screenshot_with_date(driver, "no_login_top_010.png")

            self.swipe_contents_horizontaly(driver, 250, Direction.LEFT.value)
            self.save_screenshot_with_date(driver, "no_login_top_011.png")

            self.tap_button(driver, NoLoginTop.RIGHT, WaitTime.SHORT.value)
            self.save_screenshot_with_date(driver, "no_login_top_012.png")

            self.tap_button(driver, NoLoginTop.RIGHT, WaitTime.SHORT.value)
            self.save_screenshot_with_date(driver, "no_login_top_016.png")

            self.swipe_contents_horizontaly(driver, 250, Direction.LEFT.value)
            self.save_screenshot_with_date(driver, "no_login_top_019.png")

            self.swipe_contents_horizontaly(driver, 250, Direction.RIGHT.value)
            self.save_screenshot_with_date(driver, "no_login_top_020.png")

            self.tap_button(driver, NoLoginTop.LEFT, WaitTime.SHORT.value)
            self.save_screenshot_with_date(driver, "no_login_top_021.png")
            
            # 「アカウントを作成する」をタップする
            self.tap_button(driver, NoLoginTop.CREATE_ACCOUNT, WaitTime.SHORT.value)
            self.save_screenshot_with_date(driver, "no_login_top_022.png")
            
            # 「よくあるお問い合わせ」をタップする
            self.long_tap(driver, 0.380, 0.793, 200)
            self.save_screenshot_with_date(driver, "no_login_top_023-1.png")
            self.long_tap(driver, 0.644, 0.615, 200)
            self.save_screenshot_with_date(driver, "no_login_top_023-2.png")
            
            # 「X」をタップする
            self.tap_button(driver, self.HEADER_CLOSE)
            self.save_screenshot_with_date(driver, "no_login_top_024.png")
            
            # 「組合員番号」をタップする
            self.long_tap(driver, 0.168, 0.420, 200)
            # 「5」をタップする
            self.tap_anywhere(driver, 0.378, 0.784)
            # 「電話番号」をタップする
            self.long_tap(driver, 0.168, 0.568, 200)
            #「5」をタップする　x10
            self.tap_anywhere(driver, 0.378, 0.784)
            self.tap_anywhere(driver, 0.378, 0.784)
            self.tap_anywhere(driver, 0.378, 0.784)
            self.tap_anywhere(driver, 0.378, 0.784)
            self.tap_anywhere(driver, 0.378, 0.784)
            self.tap_anywhere(driver, 0.378, 0.784)
            self.tap_anywhere(driver, 0.378, 0.784)
            self.tap_anywhere(driver, 0.378, 0.784)
            self.tap_anywhere(driver, 0.378, 0.784)
            self.tap_anywhere(driver, 0.378, 0.784)
            # 領域外タップでキーボードを閉じる
            self.long_tap(driver, 0.800, 0.568, 200)
            
            # 確認コードを送信する
            self.long_tap(driver, 0.166, 0.814, 200)
            self.save_screenshot_with_date(driver, "no_login_top_025.png")
            
            # キャンセルをタップする
            self.long_tap(driver, 0.639, 0.609, 200)
            self.save_screenshot_with_date(driver, "no_login_top_026.png")
            
            # 「←」をタップする
            self.tap_button(driver, self.BACK)
            self.save_screenshot_with_date(driver, "no_login_top_036.png")
            
            # 「ログインへ進む」をタップする
            self.tap_button(driver, NoLoginTop.GO_LOGIN, WaitTime.SHORT.value)

        except Exception as e:
            print("エラー内容:", e)
            
    
    # 任意の変化量でスワイプを実行する関数
    def swipe_contents_horizontaly(self, driver, diff, direction, sleep_time=WaitTime.SHORT.value):
        time.sleep(sleep_time)
        size = driver.get_window_size()
        # 中心座標を取得
        x = size['width'] // 2
        y = 0.665 * size['height']

        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] swipe horizontal from {x} to {x + 400} at {y}")

        driver.execute_script("mobile: swipeGesture", {
            "left": x,
            "top": y,
            "width": diff,
            "height": 0,
            "direction": direction,
            "percent": 1.0
        })
```

---

### ファイル: Appium/src/test_case/order_complete.py

```python
from common.common_const import WaitTime
from common.common_command import CommonCommand
import time
from common.common_const import Direction

class OrderComplete(CommonCommand):

    ORDER_COMPLETE = "button_order_complete"
    ORDER_CONTINUE = "button_continue_shopping"
    SELECT_BUTTON = "productCatalogSelectBtn"
    
    def do_test(self,driver):
        try:
            # 注文完了画面
            # self.tap_button(driver, self.TAB_CART)
            self.tap_button(driver, self.ORDER_COMPLETE)
            self.save_screenshot_with_date(driver, "order_complete_402.png")

            # 「注文を続ける」をタップする
            self.tap_button(driver, self.ORDER_CONTINUE)
            self.save_screenshot_with_date(driver, "order_complete_408.png")
            
            # 6月1回の企画回を選択
            # ※本番で試すときは以下をコメントアウト
            self.tap_anywhere(driver, 0.491, 0.340)
            self.tap_button(driver, self.SELECT_BUTTON)
            self.save_screenshot_with_date(driver, "order_complete_410.png")


        except Exception as e:
            print("エラー内容:", e)
```

---

### ファイル: Appium/src/test_case/order_confirm.py

```python
from common.common_const import WaitTime
from common.common_command import CommonCommand
import time
from common.common_const import Direction

class OrderConfirm(CommonCommand):

    ORDER_CONFIRM = "button_order_confirm"
    
    def do_test(self,driver):
        try:
            # 注文内容確認
            self.tap_button(driver, self.TAB_CART)
            self.tap_button(driver, self.ORDER_CONFIRM)
            self.save_screenshot_with_date(driver, "order_confirm_375.png")
            
            # 【画面制御】
            # 「←」をタップする
            self.tap_back_button(driver)
            self.tap_button(driver, self.ORDER_CONFIRM)
            self.save_screenshot_with_date(driver, "order_confirm_377.png")

            # 増資の「？」をタップする
            self.long_tap(driver, 0.158, 0.435, 200)
            self.save_screenshot_with_date(driver, "order_confirm_379.png")

            # 「X」をタップする
            self.tap_close_button(driver)
            self.save_screenshot_with_date(driver, "order_confirm_380.png")



            #【増資変更】
            # 増資額の「変更」をタップする
            self.long_tap(driver, 0.894, 0.438, 200)
            self.save_screenshot_with_date(driver, "order_confirm_382.png")
            
            # 100円の数量を「10」に設定する
            self.long_tap(driver, 0.841, 0.175, 200)
            # 「1」をタップする
            self.tap_anywhere(driver, 0.137, 0.721)
            # 「0」をタップする
            self.tap_anywhere(driver, 0.379, 0.924)
            self.save_screenshot_with_date(driver, "order_confirm_384-1.png")

            # 「キャンセル」をタップする
            self.long_tap(driver, 0.401, 0.382, 200)
            self.save_screenshot_with_date(driver, "order_confirm_384-2.png")

            
            # 増資額の「変更」をタップする
            self.long_tap(driver, 0.894, .438, 200)
            self.save_screenshot_with_date(driver, "order_confirm_385.png")
            
            # 100円の数量を「10」に設定する
            self.long_tap(driver, 0.841, 0.175, 200)
            # 「1」をタップする
            self.tap_anywhere(driver, 0.137, 0.721)
            # 「0」をタップする
            self.tap_anywhere(driver, 0.379, 0.924)
            self.save_screenshot_with_date(driver, "order_confirm_387-1.png")

            # 「←」をタップする
            self.tap_back_button(driver)
            self.save_screenshot_with_date(driver, "order_confirm_387-2.png")


            # 増資額の「変更」をタップする
            self.long_tap(driver, 0.894, .438, 200)
            self.save_screenshot_with_date(driver, "order_confirm_388.png")
            
            # 100円の数量を「10」に設定する
            self.long_tap(driver, 0.841, 0.175, 200)
            # 「1」をタップする
            self.tap_anywhere(driver, 0.137, 0.721)
            # 「0」をタップする
            self.tap_anywhere(driver, 0.379, 0.924)
            self.save_screenshot_with_date(driver, "order_confirm_390.png")

            # 「変更する」をタップする
            self.long_tap(driver, 0.658, 0.382, 200)
            self.save_screenshot_with_date(driver, "order_confirm_391.png")




            #【利用ポイント変更】
            # 利用ポイントの「変更」をタップする
            self.long_tap(driver, 0.894, 0.500, 200)
            self.save_screenshot_with_date(driver, "order_confirm_392.png")
            
            # 100Pの数量を「10」に設定する
            self.long_tap(driver, 0.710, 0.380, 300)
            # 「1」をタップする
            self.tap_anywhere(driver, 0.137, 0.721)
            # 「0」をタップする
            self.tap_anywhere(driver, 0.379, 0.924)
            # 一度フォーカスを外す
            self.long_tap(driver, 0.379, 0.124, 200)
            self.save_screenshot_with_date(driver, "order_confirm_393.png")

            # 「キャンセル」をタップする
            # 「キャンセル」が見えるまでスワイプ（一番下）
            self.swipe_vertical(driver, 800, Direction.UP.value)
            self.swipe_vertical(driver, 800, Direction.UP.value)
            self.long_tap(driver, 0.495, 0.814, 200)
            self.save_screenshot_with_date(driver, "order_confirm_394.png")

            
            # 利用ポイントの「変更」をタップする
            self.long_tap(driver, 0.894, 0.500, 200)
            self.save_screenshot_with_date(driver, "order_confirm_395.png")
            
            # 100Pの数量を「10」に設定する
            self.long_tap(driver, 0.710, 0.380, 300)
            # 「1」をタップする
            self.tap_anywhere(driver, 0.137, 0.721)
            # 「0」をタップする
            self.tap_anywhere(driver, 0.379, 0.924)
            self.save_screenshot_with_date(driver, "order_confirm_396.png")

            # 「←」をタップする
            self.tap_back_button(driver)
            self.save_screenshot_with_date(driver, "order_confirm_397.png")


            # 利用ポイントの「変更」をタップする
            self.long_tap(driver, 0.894, 0.500, 200)
            self.save_screenshot_with_date(driver, "order_confirm_398.png")
            
            # 100Pの数量を「10」に設定する
            self.long_tap(driver, 0.710, 0.380, 300)
            # 「1」をタップする
            self.tap_anywhere(driver, 0.137, 0.721)
            # 「0」をタップする
            self.tap_anywhere(driver, 0.379, 0.924)
            self.save_screenshot_with_date(driver, "order_confirm_399-1.png")

            # 一度フォーカスを外す
            self.long_tap(driver, 0.379, 0.124, 200)
            # 「ポイントを使用する」をタップする
            # 「ポイントを使用する」が見えるまでスワイプ（一番下）
            self.swipe_vertical(driver, 800, Direction.UP.value)
            self.swipe_vertical(driver, 800, Direction.UP.value)
            self.save_screenshot_with_date(driver, "order_confirm_399-2.png")

            # 「ポイントを使用する」をタップする
            self.long_tap(driver, 0.495, 0.747, 200)
            self.save_screenshot_with_date(driver, "order_confirm_400.png")

        except Exception as e:
            print("エラー内容:", e)
```

---

### ファイル: Appium/src/test_case/parukuru_promotion.py

```python
from common.common_const import WaitTime
from common.common_command import CommonCommand
import time

class PalPromo(CommonCommand):

    # パーツID
    REGISTER_BTN1 = "registerBtn1"
    FOOTER_BTN = "parukuluBtn"
    
    def do_test(self,driver):
        try:
            # パルくる便プロモーション

            
            time.sleep(2)
            # 表示確認
            self.save_screenshot_with_date(driver, "pal_promo_130.png")
            
            # # 「登録する」をタップ
            # self.tap_button(driver, self.REGISTER_BTN1, WaitTime.SHORT.value)
            # self.save_screenshot_with_date(driver, "pal_promo_132.png")

            # # モーダルの「登録する」をタップ
            # self.tap_button(driver, self.REGISTER_BTN1, WaitTime.SHORT.value)
            # self.save_screenshot_with_date(driver, "pal_promo_134.png")

            # 「対象商品一覧・登録管理」をタップ
            self.tap_button(driver, self.FOOTER_BTN, WaitTime.SHORT.value)
            self.save_screenshot_with_date(driver, "pal_promo_136.png")

            # 買い物タブをタップ
            self.tap_button(driver, self.TAB_SHOPPING, WaitTime.SHORT.value)
            self.save_screenshot_with_date(driver, "pal_promo_137.png")
            
        except Exception as e:
            print("エラー内容:", e)
```

---

### ファイル: Appium/src/test_case/select_product_catalog.py

```python
from common.common_const import WaitTime
from common.common_command import CommonCommand

class SelectProductCatalog(CommonCommand):
    
    SELECT_BUTTON = "productCatalogSelectBtn"

    def do_test(self,driver):
        try:
            # 企画回選択モーダル
            self.tap_anywhere(driver, 0.491, 0.340)
            self.save_screenshot_with_date(driver, "select_product_catalog_058.png")
            self.tap_anywhere(driver, 0.505, 0.571)
            
            self.tap_button(driver, self.SELECT_BUTTON)
            self.save_screenshot_with_date(driver, "select_product_catalog_062.png")

            # 6月1回に企画回を戻す
            self.tap_anywhere(driver, 0.491, 0.340)
            self.tap_button(driver, self.SELECT_BUTTON)

        except Exception as e:
            print("エラー内容:", e)
```

---

### ファイル: Appium/src/test_case/shopping_tab.py

```python
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
```

---

### ファイル: Appium/src/test_case/splash.py

```python
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
```

