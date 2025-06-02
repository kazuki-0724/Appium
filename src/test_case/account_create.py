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