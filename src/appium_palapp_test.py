import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
import time
from common.common_command import CommonCommand
from test_case.no_login_top import NoLoginTop
from test_case.login import Login
from test_case.account_create import AccountCreate
from test_case.splash import Splash
from test_case.shopping_tab import ShoppingTab
from test_case.item_search import ItemSearch
from test_case.select_product_catalog import SelectProductCatalog
from test_case.parukuru_promotion import PalPromo
from test_case.must_read_modal import MustReadModal
from test_case.cart import Cart
from test_case.order_confirm import OrderConfirm
from test_case.order_complete import OrderComplete
from common.common_command import CommonCommand


@pytest.fixture
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "84607e4c"
    options.app_package = "jp.co.pal_system.pochipal"
    options.app_activity = "jp.co.pal_system.pochipal.main.activity.SplashActivity"
    options.no_reset = True
    driver = webdriver.Remote("http://localhost:4723", options=options)
    yield driver
    driver.quit()


# テストケース(先頭にtest_をつける)
def stest_all_scenario(driver):
    try:
        print("\n#テスト開始######################################")

        # スプラッシュ画面
        Splash().do_test(driver)
        # 必読モーダル
        MustReadModal().do_test(driver)
        # パルくる便プロモ
        PalPromo().do_test(driver)
        # 未ログイントップ
        NoLoginTop().do_test(driver)
        # アカウント設定
        AccountCreate().do_test(driver)
        # ログイン画面
        Login().do_test(driver)
        # 通知権限の許可（座標は端末により調整）
        CommonCommand().tap_anywhere(driver, 0.498, 0.550)
        time.sleep(3)
        # 企画回選択
        SelectProductCatalog().do_test(driver)
        time.sleep(3)
        # 買い物タブ
        ShoppingTab().do_test(driver)
        # 商品検索画面
        ItemSearch().do_test(driver)
        # カゴ画面
        Cart().do_temp_test(driver)
        # 注文内容確認確認
        OrderConfirm().do_test(driver)
        # 送信完了画面
        OrderComplete().do_test(driver)


        print("\n#テスト終了######################################")
    
    except Exception as e:
        print("エラー内容:", e)


def test_sample_case(driver):
    
    try:
        print("\n#サンプルテスト開始######################################")
        OrderComplete().do_test(driver)
        print("\n#サンプルテスト終了######################################")
    
    except Exception as e:
        print("エラー内容:", e)









