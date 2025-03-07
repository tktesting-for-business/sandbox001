import os
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pymupdf4llm

########################################################
st.markdown('# 画像を保存するデモ')
file = st.file_uploader('画像をアップロードしてください.', type=['jpg', 'jpeg', 'png'])
if file:
    st.markdown(f'{file.name} をアップロードしました.')
    img_path = os.path.join(IMG_PATH, file.name)
    # 画像を保存する
    with open(img_path, 'wb') as f:
        f.write(file.read())
        
    # 保存した画像を表示
    img = Image.open(img_path)
    st.image(img)        
########################################################

filename = "有価証券報告書（2024年3月期）.pdf"
md_text = pymupdf4llm.to_markdown(filename)
#st.write(md_text)
st.code(md_text, language='python')

#with open("output.md", "w", encoding="utf-8") as f:
#    f.write(md_text)
    
#IMG_PATH = 'imgs'
#img_path = os.path.join(IMG_PATH, "output.md")
# 画像を保存する
#with open(img_path, 'wb') as f:
#    f.write(md_text)

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
