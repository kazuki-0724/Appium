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
from PIL import Image, ImageDraw
import os
import random


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
        ans = input("パルくる便プロモ・必読モーダル・カゴは空・赤バッチ無しの状態ですか？ (Y/N): ").strip().lower()
        if ans != 'y':
            print("準備をしてから再度実行してください。")
            return
        # test_splash(driver)
        test_no_login_top(driver)
        test_login(driver)
        # 通知権限の許可
        CommonCommand().tap_anywhere(driver, 0.498, 0.550)
        time.sleep(3)
        test_select_product_catalog(driver)
        test_must_read_modal(driver)
        test_parukuru_promotion(driver)
        switch_select_product_catalog(driver)
        
    except Exception as e:
        print("エラー内容:", e)


# 【事前準備】カゴを完全に空にしておく&&カタログ表示が初期状態 
def test_2nd_block(driver):
    try:
        ans = input("カゴを空の状態にしましたか？ カタログ表示は初期状態ですか？(Y/N): ").strip().lower()
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
        ans = input("カゴの中は「299」の商品1つだけですか？ (Y/N): ").strip().lower()
        if ans != 'y':
            print("カゴ商品を「299」の商品のみにしてください")
            return
        test_cart1(driver)
    except Exception as e:
        print("エラー内容:", e)


# 【事前準備】「test_3rd_block」を事前に実行しておく
def test_4th_block(driver):
    try:
        ans = input("事前に「test_3rd_block」を実行していますか？ (Y/N): ").strip().lower()
        if ans != 'y':
            print("事前に「test_3rd_block」を実行してください")
            return
        test_cart2(driver)
    except Exception as e:
        print("エラー内容:", e)


#  【事前準備】特になし
def test_5th_block(driver):
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


def test_cart1(driver):
    try:
        print("\n#カゴ画面テスト1開始######################################")
        Cart().do_test1(driver)
        print("\n#カゴ画面テスト1終了######################################")
    except Exception as e:
        print("エラー内容:", e)


def test_cart2(driver):
    try:
        print("\n#カゴ画面テスト2開始######################################")
        Cart().do_test2(driver)
        print("\n#カゴ画面テスト2終了######################################")
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
        

def test_monkey_test(driver):
        """
        モンキーのテストを実行する関数
        """
        cmd = CommonCommand()
        try:
            for i in range(10): # n回のモンキーテストを実行
                x = random.uniform(0.1, 0.9)  # ランダムなX座標
                y = random.uniform(0.1, 0.9)  # ランダ
                cmd.save_screenshot_with_date(driver, filename=f"monkey_test_{i}_before.png", directory="monkey")
                add_transparent_yellow_circle_with_red_center(
                    f"monkey_test_{i}_before.png",
                    center_x=int(x * driver.get_window_size()['width']),
                    center_y=int(y * driver.get_window_size()['height'])
                )
                cmd.long_tap(driver, x, y, 200)
                cmd.save_screenshot_with_date(driver, filename=f"monkey_test_{i}_after.png", directory="monkey")
        
        except Exception as e:
            print("エラー内容:", e)
            return


def add_transparent_yellow_circle_with_red_center(input_path, center_x, center_y):
        try:
            # 画像をRGBAモードで開く
            # 半透明の描画にはRGBAモードが必要
            image = Image.open(os.path.join("../reports/monkey", input_path)).convert("RGBA")

            # 描画用の透明なレイヤーを作成
            # 元の画像と同じサイズとRGBAモードで、完全に透明な画像を作る
            transparent_layer = Image.new("RGBA", image.size, (0, 0, 0, 0))
            draw = ImageDraw.Draw(transparent_layer)

            # 外側の黄色い半透明の丸を描画
            # RGBA(255, 255, 0, 128) は「黄色で半透明」を意味する
            blue_transparent = (0, 0, 200, 128) 
        
            # 描画する丸のバウンディングボックスを計算
            outer_bbox = [
                (center_x - 30, center_y - 30),
                (center_x + 30, center_y + 30)
            ]
            draw.ellipse(outer_bbox, fill=blue_transparent)
        
            # 内側の赤い丸を描画
            red = (255, 0, 0, 255) # 赤色で完全に不透明
            inner_bbox = [
                (center_x - 5, center_y - 5),
                (center_x + 5, center_y + 5)
            ]
            draw.ellipse(inner_bbox, fill=red)

            # 元の画像の上に透明なレイヤーを合成
            # `Image.alpha_composite`で透明度を考慮して合成する
            result_image = Image.alpha_composite(image, transparent_layer)
        
            # 最終的な画像をPNG形式で保存
            # PNGは透明度をサポートしているため推奨
            result_image.save(os.path.join("../reports/monkey", input_path), "PNG")
            print(f"画像が /reports/monkey/{input_path} に保存されました。")

        except FileNotFoundError:
            print(f"エラー: 指定されたファイルが見つかりません - {input_path}")
        except Exception as e:
            print(f"エラーが発生しました: {e}")