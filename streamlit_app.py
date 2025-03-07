import os
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pymupdf4llm

########################################################
uploaded_file = "決算説明資料（2022年3月期）.pdf"
md_text = pymupdf4llm.to_markdown(uploaded_file)
st.code(md_text, language='python')

#IMG_PATH = 'imgs'
#uploaded_file = st.file_uploader('Choose a PDF file')
#if uploaded_file is not None:
#    st.markdown(f'{uploaded_file.name} をアップロードしました.')
#    img_path = os.path.join(IMG_PATH, uploaded_file.name)
#    
#    # 保存したPDFをmarkdown表示
#    st.write(img_path)
#    md_text = pymupdf4llm.to_markdown(img_path)
#    st.code(md_text, language='python')
#else:
#    st.info('☝️ Upload a file')

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
