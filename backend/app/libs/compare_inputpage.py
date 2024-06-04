import pandas as pd

def compare_inputpage(input_df, result_df):
    # sub_title_inputとsub_title_resultの並び順をチェック
    input_subtitles = input_df['sub_title_input'].tolist()
    result_subtitles = result_df['sub_title_result'].tolist()
    
    check_order = []
    for i in range(len(input_subtitles)):
        if i == len(input_subtitles) - 1:  # 最後の要素の場合
            if input_subtitles[i] in result_subtitles:
                check_order.append('')
            else:
                check_order.append('Item Missing or Created with Image')
        else:  # 最後の要素でない場合
            if input_subtitles[i] in result_subtitles and input_subtitles[i+1] in result_subtitles:
                index_current = result_subtitles.index(input_subtitles[i])
                index_next = result_subtitles.index(input_subtitles[i+1])
                if index_current < index_next:
                    check_order.append('')
                else:
                    check_order.append('Mismatched Items')
            else:
                if input_subtitles[i] not in result_subtitles:
                    check_order.append('Item Missing or Created with Image')
                elif input_subtitles[i+1] not in result_subtitles:
                    check_order.append('Next Item Missing or Created with Image')
    
    input_df['check_order'] = check_order
    
    # sub_title_inputとsub_title_resultの文言が完全一致しているか確認
    check_text = []
    for subtitle_input in input_df['sub_title_input']:
        if subtitle_input in result_df['sub_title_result'].tolist():
            check_text.append(True)
        else:
            check_text.append(False)
    
    input_df['check_text'] = check_text
    
    # dfをdictに変換して返す
    result_dict = input_df.to_dict(orient='records')
    return result_dict