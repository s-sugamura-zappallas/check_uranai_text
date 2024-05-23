import pandas as pd
import numpy as np

def compare_toppage(html_df, csv_df):
    # DataFrameのコピーを作成
    result_df = html_df.copy()

    # price_html と price_csv 列を文字列に変換
    html_df['price_html'] = html_df['price_html'].astype(str)
    csv_df['price_csv'] = csv_df['price_csv'].astype(str)

    # menu、caption、price を組み合わせた列を作成
    html_df['combined_html'] = html_df['menu_html'] + html_df['caption_html'] + html_df['price_html']
    csv_df['combined_csv'] = csv_df['menu_csv'] + csv_df['caption_csv'] + csv_df['price_csv']

    # combined_csv が combined_html に含まれているか確認
    result_df['is_same_set'] = html_df['combined_html'].isin(csv_df['combined_csv'])

    # 一致するメニュー、キャプション、価格を抽出
    result_df['matched_menu_csv'] = result_df['menu_html'].where(result_df['is_same_set'], '')
    result_df['matched_caption_csv'] = result_df['caption_html'].where(result_df['is_same_set'], '')
    result_df['matched_price_csv'] = result_df['price_html'].where(result_df['is_same_set'], '')

    # 異なる項目を特定するための列を追加
    result_df['diff_menu'] = (result_df['menu_html'] != result_df['matched_menu_csv'])
    result_df['diff_caption'] = (result_df['caption_html'] != result_df['matched_caption_csv'])
    result_df['diff_price'] = (result_df['price_html'] != result_df['matched_price_csv'])

    # is_same_setがFalseのとき、個別項目の比較を行う (修正箇所)
    # is_same_setがFalseの行に対して処理を行う
    for index in result_df.index[~result_df['is_same_set']]:
        
        menu_html = result_df.loc[index, 'menu_html']
        caption_html = result_df.loc[index, 'caption_html']
        price_html = result_df.loc[index, 'price_html']

        menu_match = False
        caption_match = False
        price_match = False

        #print(f"Checking HTML row {index}: menu_html={menu_html}, caption_html={caption_html}, price_html={price_html}")

    # csv_dfの全行をチェック
        for csv_index, csv_row in csv_df.iterrows():
            menu_csv = csv_row['menu_csv']
            caption_csv = csv_row['caption_csv']
            price_csv = csv_row['price_csv']

            #print(f"Comparing with CSV row {csv_index}: menu_csv={menu_csv}, caption_csv={caption_csv}, price_csv={price_csv}")


        # menuが一致するかチェック
            if menu_html == menu_csv:
                menu_match = True
        # captionが一致するかチェック
            if caption_html == caption_csv:
                caption_match = True
        # menuまたはcaptionが一致する場合にpriceを比較
            if menu_html == menu_csv or caption_html == caption_csv:
                #print(f"Checking types: HTML price type = {type(price_html)}, CSV price type = {type(price_csv)}")

                # price_csvをnumpy.int64に変換
                try:
                    price_html_float = float(price_html)
                    price_csv_float = float(price_csv)
                    #print(f"Checking types after conversion: HTML price type = {type(price_html_float)}, CSV price type = {type(price_csv_float)}")
                    if price_html_float == price_csv_float:
                        price_match = True
                        #print(f"Price match found: HTML price = {price_html_float}, CSV price = {price_csv_float}")
                except ValueError as e:
                    print(f"Error converting prices to float: {e}")

    # diff_menuとdiff_captionを設定
        result_df.loc[index, 'diff_menu'] = not menu_match
        result_df.loc[index, 'diff_caption'] = not caption_match
    # diff_priceを設定
        result_df.loc[index, 'diff_price'] = not price_match



    # diff_menu, diff_caption, diff_price を整数型に変換
    result_df['diff_menu'] = result_df['diff_menu'].astype(int)
    result_df['diff_caption'] = result_df['diff_caption'].astype(int)
    result_df['diff_price'] = result_df['diff_price'].astype(int)

    selected_columns = ['menu_html', 'caption_html', 'price_html', 'is_same_set', 'diff_menu', 'diff_caption', 'diff_price']
    result_dict = result_df[selected_columns].to_dict(orient='records')

    return result_dict