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


    def do_test(self,driver):
        try:
            # カゴ画面
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