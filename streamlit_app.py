import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# プログラム開始時にPDFファイルのパスを変数に指定
pdf_file_path = "FY2024_3Q_print.pdf"  # ここにPDFファイルのパスを指定

########################################################
from pdf2image import convert_from_path
import easyocr
import io
from PIL import Image

def pdf_to_text_easyocr(pdf_path, use_gpu=False, languages=['ja', 'en']):
    """
    PDFファイルを画像に変換し、EasyOCRを使って各ページからテキストを抽出する。

    Args:
        pdf_path (str): PDFファイルへのパス。
        use_gpu (bool): EasyOCRでGPUを使用するかどうか (True/False)。
        languages (list): EasyOCRで使用する言語のリスト (例: ['ja', 'en'])。

    Returns:
        str: 抽出されたテキスト (全ページ分、改行で連結)。
    """

    try:
        # PDFをPIL Imageオブジェクトのリストに変換
        images = convert_from_path(pdf_path)

        # EasyOCRリーダーの初期化
        reader = easyocr.Reader(languages, gpu=use_gpu)
        #reader = easyocr.Reader(['en', 'ja'])

        all_text = []
        for i, image in enumerate(images):
            # 各ページをEasyOCRで処理
            print(f"Processing page {i+1}...")

            # PIL ImageをEasyOCRに渡す
            results = reader.readtext(image, paragraph=True)  #段落として結合

            # 各ページの結果を結合
            page_text = " ".join([result[1] for result in results])
            all_text.append(page_text)

        # 全ページのテキストを改行で結合
        full_text = "\n\n".join(all_text)
        return full_text

    except Exception as e:
        print(f"An error occurred: {e}")
        return ""

extracted_text = pdf_to_text_easyocr(pdf_file_path, use_gpu=False) # GPU使わない場合
st.write(extracted_text)
########################################################
# pdfplumberライブラリをインポート
#import pdfplumber


# PDFファイルを開く
#with pdfplumber.open(pdf_file_path) as pdf:
#    # PDFの各ページに対して処理を行う
#    for page in pdf.pages:
#        # ページからテキストデータを抽出
#        text = page.extract_text()
#        
#        # 抽出したテキストデータを出力
#        st.write(text)
########################################################
#from markitdown import MarkItDown
#md = MarkItDown()
#result = md.convert(pdf_file_path)
#st.write(result.text_content)
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
