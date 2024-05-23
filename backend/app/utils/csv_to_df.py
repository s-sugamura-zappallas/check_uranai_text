import io
import pandas as pd

def csv_to_df(csv_file):
    """CSV ファイルを pandas DataFrame に変換する関数。
    Args:
        csv_file: CSV ファイルのバイナリデータ。
    Returns:
        pandas DataFrame。
    """
    # StringIO を使用して pandas DataFrame を作成する
    df = pd.read_csv(csv_file, usecols=['メニュー名', 'キャプション', '金額(税込)'])
    
    # カラム名を変更する
    df = df.rename(columns={'メニュー名': 'menu_csv', 'キャプション': 'caption_csv', '金額(税込)': 'price_csv'})
    
    return df