import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

########################################################
from pdfminer.high_level import extract_text

def extract_text_from_pdf(pdf_path):
    """
    PDFファイルからテキストを抽出する (ToUnicode CMapを自動的に利用)。

    Args:
        pdf_path (str): PDFファイルへのパス。

    Returns:
        str: 抽出されたテキスト。
    """
    text = extract_text(pdf_path)
    return text

########################################################
pdf_file = "your_pdf_file.pdf"  # 抽出したいPDFファイル名
extracted_text = extract_text_from_pdf("BSC.pdf")
st.write(extracted_text)

########################################################
from markitdown import MarkItDown
md = MarkItDown()
#result = md.convert("FY2024_3Q.pdf")
#html_text = convert_cid_string(result.text_content, "html_entity")
#st.write(html_text)
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
