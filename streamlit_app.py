import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("BSC.pdf")
st.write(result.text_content)

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
