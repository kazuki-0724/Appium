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


# 【事前準備】パルくる便プロモ・必読モーダルの準備をする
def test_1st_block(driver):
    try:
        ans = input("パルくる便プロモ・必読モーダルの準備をしましたか？ (Y/N): ").strip().lower()
        if ans != 'y':
            print("パルくる便プロモ・必読モーダルの準備をしてから再度実行してください。")
            return
        # test_splash(driver)
        test_no_login_top(driver)
        test_login(driver)
        # 通知権限の許可（座標は端末により調整）
        CommonCommand().tap_anywhere(driver, 0.498, 0.550)
        time.sleep(3)
        test_select_product_catalog(driver)
        test_must_read_modal(driver)
        test_parukuru_promotion(driver)
        switch_select_product_catalog(driver)
        
    except Exception as e:
        print("エラー内容:", e)


# 【事前準備】カゴを完全に空にしておく
def test_2nd_block(driver):
    try:
        ans = input("カゴを空の状態にしましたか？ (Y/N): ").strip().lower()
        if ans != 'y':
            print("カゴを空にしてから再度実行してください。")
            return
        test_shopping_tab(driver)
        test_item_search(driver)
    except Exception as e:
        print("エラー内容:", e)


# 【事前準備】カゴに「111」の商品だけにしておく
def test_3rd_block(driver):
    try:
        ans = input("カゴの中は「111」の商品1つだけですか？ (Y/N): ").strip().lower()
        if ans != 'y':
            print("カゴない商品を「111」の商品のみにしてください")
            return
        test_cart(driver)
    except Exception as e:
        print("エラー内容:", e)


#  【事前準備】特になし
def test_4th_block(driver):
    try:
        test_order_confirm(driver)
        test_order_complete(driver)
    except Exception as e:
        print("エラー内容:", e)





################################################
# 各テストケースを単独で実行するメソッド###########
################################################

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
        print("\n#企画回選択(6月1回)テスト開始######################################")
        SelectProductCatalog().do_test(driver)
        print("\n#企画回選択(6月1回)終了企画回選択######################################")
    except Exception as e:
        print("エラー内容:", e)


def switch_select_product_catalog(driver):
    try:
        print("\n#企画回選択(6月1回⇒2回⇒1回)開始######################################")
        SelectProductCatalog().do_test2(driver)
        print("\n#企画回選択(6月1回⇒2回⇒1回)テスト終了######################################")
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