import streamlit as st

# 選択オプション
option = st.selectbox(
    "表示する内容を選んでください",
    ("テキスト", "画像", "データフレーム")
)

# 動的にコンテンツを表示
if option == "テキスト":
    st.write("これはテキストです。")
elif option == "画像":
    st.image("https://example.com/sample.jpg")
elif option == "データフレーム":
    import pandas as pd
    df = pd.DataFrame({
        "列1": [1, 2, 3],
        "列2": ["A", "B", "C"]
    })
    st.write(df)
