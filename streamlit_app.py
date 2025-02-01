import streamlit as st
import pandas as pd

def load_iris_data():
    """
    データ読み込み, cacheにして最適化を行う
    """
    iris_data = load_iris()
    df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
    labels = iris_data.target_names[iris_data.target]
    return df, labels

st.write('### アイリスデータを見ていく')
df, labels = load_iris_data()

def show_heatmap(df):
    """
    各特徴の相関ヒートマップをみる
    """
    fig, ax = plt.subplots(figsize=(10,10))
    sns.heatmap(df.corr(), annot=True, ax=ax)
    st.pyplot(fig)

st.write('特徴ごとの相関のHeatMap表示')
show_heatmap(df)

st.write('DataFrameの表示')
st.write(df)
