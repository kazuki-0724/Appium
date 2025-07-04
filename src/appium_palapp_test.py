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
def test_all_case(driver):
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
        Cart().do_test(driver)
        # 注文内容確認確認
        OrderConfirm().do_test(driver)
        # 送信完了画面
        OrderComplete().do_test(driver)


        print("\n#テスト終了######################################")
    
    except Exception as e:
        print("エラー内容:", e)


# 各テストケースを単独で実行するメソッド
def test_splash(driver):
    try:
        print("\n#スプラッシュ画面テスト開始######################################")
        Splash().do_test(driver)
        print("\n#スプラッシュ画面テスト終了######################################")
    except Exception as e:
        print("エラー内容:", e)


def test_must_read_modal(driver):
    try:
        print("\n#必読モーダルテスト開始######################################")
        MustReadModal().do_test(driver)
        print("\n#必読モーダルテスト終了######################################")
    except Exception as e:
        print("エラー内容:", e)


def test_parukuru_promotion(driver):
    try:
        print("\n#パルくる便プロモテスト開始######################################")
        PalPromo().do_test(driver)
        print("\n#パルくる便プロモテスト終了######################################")
    except Exception as e:
        print("エラー内容:", e)


def test_no_login_top(driver):
    try:
        print("\n#未ログイントップテスト開始######################################")
        NoLoginTop().do_test(driver)
        print("\n#未ログイントップテスト終了######################################")
    except Exception as e:
        print("エラー内容:", e)


def test_account_create(driver):
    try:
        print("\n#アカウント作成テスト開始######################################")
        AccountCreate().do_test(driver)
        print("\n#アカウント作成テスト終了######################################")
    except Exception as e:
        print("エラー内容:", e)


def test_login(driver):
    try:
        print("\n#ログイン画面テスト開始######################################")
        Login().do_test(driver)
        print("\n#ログイン画面テスト終了######################################")
    except Exception as e:
        print("エラー内容:", e)


def test_select_product_catalog(driver):
    try:
        print("\n#企画回選択テスト開始######################################")
        SelectProductCatalog().do_test(driver)
        print("\n#企画回選択テスト終了######################################")
    except Exception as e:
        print("エラー内容:", e)


def test_shopping_tab(driver):
    try:
        print("\n#買い物タブテスト開始######################################")
        ShoppingTab().do_test(driver)
        print("\n#買い物タブテスト終了######################################")
    except Exception as e:
        print("エラー内容:", e)


def test_item_search(driver):
    try:
        print("\n#商品検索画面テスト開始######################################")
        ItemSearch().do_test(driver)
        print("\n#商品検索画面テスト終了######################################")
    except Exception as e:
        print("エラー内容:", e)


def test_cart(driver):
    try:
        print("\n#カゴ画面テスト開始######################################")
        Cart().do_test(driver)
        print("\n#カゴ画面テスト終了######################################")
    except Exception as e:
        print("エラー内容:", e)


def test_order_confirm(driver):
    try:
        print("\n#注文内容確認テスト開始######################################")
        OrderConfirm().do_test(driver)
        print("\n#注文内容確認テスト終了######################################")
    except Exception as e:
        print("エラー内容:", e)


def test_order_complete(driver):
    try:
        print("\n#注文完了画面テスト開始######################################")
        OrderComplete().do_test(driver)
        print("\n#注文完了画面テスト終了######################################")
    except Exception as e:
        print("エラー内容:", e)


def test_sample_case(driver):
    try:
        print("\n#サンプルテスト開始######################################")
        OrderComplete().do_test(driver)
        print("\n#サンプルテスト終了######################################")
    
    except Exception as e:
        print("エラー内容:", e)









