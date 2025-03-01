import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

########################################################
# pdfplumberライブラリをインポート
import pdfplumber

# プログラム開始時にPDFファイルのパスを変数に指定
pdf_file_path = "FY2024_3Q.pdf"  # ここにPDFファイルのパスを指定

# PDFファイルを開く
with pdfplumber.open(pdf_file_path) as pdf:
    # PDFの各ページに対して処理を行う
    for page in pdf.pages:
        # ページからテキストデータを抽出
        text = page.extract_text()
        
        # 抽出したテキストデータを出力
        st.write(text)

########################################################
from markitdown import MarkItDown
md = MarkItDown()
#result = md.convert("challenge_dh7th_en.pdf")
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
