import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# プログラム開始時にPDFファイルのパスを変数に指定
pdf_file_path = "FY2024_3Q_print.pdf"  # ここにPDFファイルのパスを指定

########################################################
from pdf2image import convert_from_path
import pytesseract  # または easyocr

# Tesseractの実行ファイルパス設定 (Windowsの場合)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def pdf_to_text_ocr(pdf_path):
    """
    PDFを画像に変換し、OCRでテキスト抽出 (pytesseract使用)。
    """
    all_text = ""
    images = convert_from_path(pdf_path)  # PDFを画像(PIL Image)のリストに変換
    for i, image in enumerate(images):
        # 各ページをOCR
        text = pytesseract.image_to_string(image, lang='jpn')
        all_text += f"--- Page {i+1} ---\n" + text + "\n"
    return all_text

extracted_text = pdf_to_text_ocr(pdf_file_path)
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
