import os
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pymupdf4llm

########################################################
IMG_PATH = "."
uploaded_file = st.file_uploader('Choose a file')
if uploaded_file is not None:
    st.markdown(f'{uploaded_file.name} をアップロードしました.')
    img_path = os.path.join(IMG_PATH, uploaded_file.name)
    # 画像を保存する
    with open(img_path, 'wb') as f:
        f.write(uploaded_file.read())        

    # 保存した画像を表示
    img = Image.open(img_path)
    st.image(img)  
else:
    st.info('☝️ Upload a CSV file')

########################################################
#filename = "有価証券報告書（2024年3月期）.pdf"
#md_text = pymupdf4llm.to_markdown(filename)
#st.code(md_text, language='python')

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
