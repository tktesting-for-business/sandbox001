import streamlit as st
import pandas as pd
import numpy as np

# サンプルデータを生成
data = pd.DataFrame({
    '日付': pd.date_range(start='2023-01-01', end='2023-01-10'),
    '値': np.random.randint(1, 100, size=10)
})

# 折れ線グラフをプロット
st.write('折れ線グラフ:')
st.line_chart(data.set_index('日付'))
