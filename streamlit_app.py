import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("challenge_dh7th_en.pdf")
st.write(result.text_content)

########################################################

import re
from urllib.parse import quote

def cid_to_html_entity(match):
    """
    CIDコード (例: /CID+1234) をHTML数値文字参照 (例: Ӓ) に変換する。

    Args:
        match: re.Match オブジェクト (正規表現のマッチ結果)

    Returns:
        str: HTML数値文字参照
    """
    cid_code = int(match.group(1))  # CIDコードを整数として取得
    return f"&#{cid_code};"

def cid_to_url_encoded(match):
    """
    CIDコードをパーセントエンコーディングされた文字列に変換する。

    Args:
        match: re.Matchオブジェクト

    Returns:
        str: パーセントエンコーディングされた文字列
    """
    cid_code = int(match.group(1))
    # chr() でUnicode文字に変換し、その後URLエンコード
    char = chr(cid_code)
    return quote(char, encoding='utf-8')


def cid_to_unicode_literal(match):
    """
    CIDコードをUnicodeリテラル表現 (例: \u3042) に変換する。

    Args:
        match: re.Matchオブジェクト

    Returns:
        str: Unicodeリテラル表現
    """

    cid = int(match.group(1))
    try:
      # CIDをUnicodeコードポイントとして解釈
      char = chr(cid)
      # Unicodeコードポイントを16進数で表現
      hex_code = hex(ord(char))[2:].upper()
      # 4桁になるように0でパディング
      hex_code_padded = hex_code.zfill(4)
      return '\\u' + hex_code_padded
    except ValueError:  #chr()の範囲外
        return match.group(0) #元の文字列を返す

def convert_cid_string(cid_string, conversion_type="html_entity"):
    """
    CID文字列を、指定された形式に変換する。

    Args:
        cid_string (str): CIDコードを含む文字列 (例: "/CID+1234/CID+5678")
        conversion_type (str): 変換タイプ ("html_entity", "url_encode", "unicode_literal")

    Returns:
        str: 変換された文字列
    """

    if conversion_type == "html_entity":
        return re.sub(r"/CID\+(\d+)", cid_to_html_entity, cid_string)
    elif conversion_type == "url_encode":
        return re.sub(r"/CID\+(\d+)", cid_to_url_encoded, cid_string)
    elif conversion_type == "unicode_literal":
        return re.sub(r"/CID\+(\d+)", cid_to_unicode_literal, cid_string)

    else:
        raise ValueError("Invalid conversion_type. Choose 'html_entity', 'url_encode', or 'unicode_literal'.")



def test_conversion():
    test_strings = [
        "/CID+8271/CID+8272/CID+8305",  # 日本語の例 (あいう)
        "/CID+65/CID+66/CID+67",       # アルファベットの例 (ABC)
        "/CID+12345/CID+9876",          # 大きな数値、範囲外になりうる数値
        "This is a test with /CID+97 and /CID+98.", # 通常の文字と混在
        "/CID+", # 不正な形式
        "/CID+ABC",
        "/CID+-123"
    ]

    conversion_types = ["html_entity", "url_encode", "unicode_literal"]

    for cid_str in test_strings:
        print(f"Original: {cid_str}")
        for conv_type in conversion_types:
            converted = convert_cid_string(cid_str, conv_type)
            print(f"  {conv_type.ljust(15)}: {converted}")  # .ljust() で左寄せ
        print("-" * 30)


if __name__ == "__main__":
    test_conversion()

    # 使用例： PDFから抽出した文字列を変換
    extracted_text_from_pdf = "/CID+8251/CID+8252/CID+8253/CID+1234/CID+45/CID+67"  #PDFから抽出された文字列の例
    html_text = convert_cid_string(extracted_text_from_pdf, "html_entity")

    print("\n--- Example Usage ---")
    print(f"Original (from PDF): {extracted_text_from_pdf}")
    print(f"HTML Entities      : {html_text}")

    # HTMLファイルに出力する例
    html_output = f"""<!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>CID Converted Text</title>
    </head>
    <body>
        <p>{html_text}</p>
    </body>
    </html>
    """

    with open("output.html", "w", encoding="utf-8") as f:
        f.write(html_output)
    print("Converted HTML saved to output.html")
########################################################


df = pd.DataFrame({'A': range(5),
                   'B': [x**2 for x in range(5)],
                   'C': [x**3 for x in range(5)]})
 

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)
st.write(df)

def show_heatmap(df):
    """
    各特徴の相関ヒートマップをみる
    """
    fig, ax = plt.subplots(figsize=(10,10))
    sns.heatmap(df.corr(), annot=True, ax=ax)
    st.pyplot(fig)

st.write('特徴ごとの相関のHeatMap表示')
show_heatmap(df)
