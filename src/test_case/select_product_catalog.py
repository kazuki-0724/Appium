from common.common_const import WaitTime
from common.common_command import CommonCommand

class SelectProductCatalog(CommonCommand):
    
    SELECT_BUTTON = "productCatalogSelectBtn"

    def do_test(self,driver):
        try:
            # 企画回選択モーダル
            self.tap_anywhere(driver, 0.491, 0.340)
            self.save_screenshot_with_date(driver, "select_product_catalog_058.png")
            
            self.tap_button(driver, self.SELECT_BUTTON)
            #self.save_screenshot_with_date(driver, "select_product_catalog_062.png")

            
            # 6月2回に企画回を変更
            self.tap_anywhere(driver, 0.505, 0.571)
            #self.tap_anywhere(driver, 0.491, 0.340)
            #self.tap_button(driver, self.SELECT_BUTTON)

        except Exception as e:
            print("エラー内容:", e)
    
    def do_test2(self,driver):
        try:
            # 企画回選択バナーをタップ
            self.tap_anywhere(driver, 0.491, 0.340)
            # 6月2回に企画回を変更
            self.tap_anywhere(driver, 0.505, 0.571)
            self.save_screenshot_with_date(driver, "select_product_catalog_059.png")
            self.tap_button(driver, self.SELECT_BUTTON)
            self.save_screenshot_with_date(driver, "select_product_catalog_060.png")
            
            # 企画回選択バナーをタップ
            self.tap_anywhere(driver, 0.491, 0.340)
            # 6月1回に企画回を変更
            self.tap_anywhere(driver, 0.491, 0.340)
            self.tap_button(driver, self.SELECT_BUTTON)
            self.save_screenshot_with_date(driver, "select_product_catalog_062.png")
            
        except Exception as e:
            print("エラー内容:", e)