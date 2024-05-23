import pandas as pd
from bs4 import BeautifulSoup
import re

def html_to_df_rsa(html_str: str) -> pd.DataFrame:
    # HTMLをパースする
    soup = BeautifulSoup(html_str, 'html.parser')

    # メニュー名、キャプション、金額を格納するリストを初期化する
    menu_names = []
    captions = []
    prices = []

    # <div class="appraisal_menu">の要素を取得する
    appraisal_menus = soup.find_all('div', class_='appraisal_menu')

    for menu in appraisal_menus:
        # メニュー名を取得する
        menu_name = menu.find('a').find('p').text.strip()
        menu_names.append(menu_name)

        # キャプションを取得する
        caption = menu.find('p', class_='description').text.strip()
        captions.append(caption)

        # 金額を取得し、数値に変換する
        price_str = menu.find('p', class_='price').find('span').text.strip()
        price = int(price_str.replace(',', '').replace('円', '').replace('(税込)', '').replace('価格', '').strip())
        prices.append(price)

    # データフレームを作成する
    df = pd.DataFrame({
        'menu_html': menu_names,
        'caption_html': captions,
        'price_html': prices
    })

    return df



def html_to_df_zap(html_str: str) -> pd.DataFrame:
    print("start html_to_df_zap")
    # HTMLをパースする
    soup = BeautifulSoup(html_str, 'html.parser')

    # メニュー名、キャプション、金額を格納するリストを初期化する
    menu_names = []
    captions = []
    prices = []

    # <div class="severalmenu">の要素を取得する
    several_menus = soup.find_all('div', class_='severalmenu')
    for menu in several_menus:
        # メニュー名を取得する
        menu_name_element = menu.find('div', class_='menu_info').find('h3')
        if menu_name_element:
            menu_name = menu_name_element.text.strip()
            menu_names.append(menu_name)
        else:
            menu_names.append(None)

        # キャプションを取得する
        caption_element = menu.find('p', class_='caption')
        if caption_element:
            caption = caption_element.text.strip()
            captions.append(caption)
        else:
            captions.append(None)

        # 金額を取得し、数値に変換する
        price_element = menu.find('p', class_='price_info')
        if price_element:
            price_str = price_element.text.strip()
            print(f"Pattern 1: {price_str}")
            price = int(re.sub(r'[^\d]', '', price_str))
        else:
            price_element = menu.find('div', class_='price_info')
            if price_element:
                price_str = price_element.text.strip()
                print(f"Pattern 2: {price_str}")
                price = int(re.sub(r'[^\d]', '', price_str))
            else:
                price_element = menu.find('div', class_='price_normal')
                if price_element:
                    price_str = price_element.text.strip()
                    print(f"Pattern 3: {price_str}")
                    price = int(re.sub(r'[^\d]', '', price_str))
                else:
                    print("No price found")
                    price = 0
        prices.append(price)

    # データフレームを作成する
    df = pd.DataFrame({
        'menu_html': menu_names,
        'caption_html': captions,
        'price_html': prices
    })

    return df