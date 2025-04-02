import os
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pymupdf4llm


########################################################
import yfinance as yf

# 大和ハウスの株価データを取得
ticker_symbol = "1925.T"
st.write(ticker_symbol)
ticker_data = yf.Ticker(ticker_symbol)

# 過去1週間のデータを取得
#hist_data = ticker_data.history(period="1wk")

# 取得したデータを表示
#st.write(hist_data)

ticker_info = yf.Ticker(ticker_symbol)

# 貸借対照表
balance_sheet = ticker_info.balance_sheet
#st.write("Balance Sheet")
balance_sheet.columns = balance_sheet.columns[::-1]
#st.write(balance_sheet)

def show_balance_sheet_item(item):
    if item in balance_sheet.index:
        item_data = balance_sheet.loc[item]
        st.write(f"\n--- " + item + " for " + ticker_symbol + " ---")
        st.write(item_data)

#show_balance_sheet_item("Working Capital")

# 損益計算書
income_stmt = ticker_info.income_stmt #年単位
#income_stmt = ticker_info.quarterly_income_stmt #4ヶ月単位
st.write("Income Statement")
income_stmt.columns = income_stmt.columns[::-1]
#st.write(income_stmt)

def income_stmt_items(item):
    if item in income_stmt.index:
        item_data = income_stmt.loc[item]
        return item_data

Total_Revenue =income_stmt_items("Total Revenue")
Gross_Profit =income_stmt_items("Gross Profit")
Operating_Income =income_stmt_items("Operating Income")
Pretax_Income =income_stmt_items("Pretax Income")
Net_Income =income_stmt_items("Net Income")

df_output = pd.concat([Total_Revenue, Gross_Profit,Operating_Income,Pretax_Income,Net_Income], axis=1) # axis=1 で列方向に結合
st.write(df_output.T)
st.line_chart(df_output,x)

# キャッシュフロー
#cash_flow = ticker_info.cash_flow

# 配当金
#dividends = ticker_info.dividends

# 決算日
#earnings_dates = ticker_info.earnings_dates

# 財務諸表
financials = ticker_info.financials
#st.write(financials)

# 企業情報
#info = ticker_info.info

# ニュース
#news = ticker_info.news

# 四半期貸借対照表
#quarterly_balance_sheet = ticker_info.quarterly_balance_sheet

# 四半期キャッシュフロー
#quarterly_cash_flow = ticker_info.quarterly_cash_flow

# 四半期財務諸表
#quarterly_financials = ticker_info.quarterly_financials

########################################################
import requests
import json

REFRESH_TOKEN = "eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.GVCUJEhqSvCE_WRCOqSOgj6Dvu1oY0Oqd36JEexRVkKASxZbIljwauEnNl4zYWhIkSfd1EXkOZzEh8SHT0IldNYbV9Nnk0YJhN3rwzo5YEciDhBQ-sD3raV9woHDbEAcfOcgbddTUJ2-shH-E_boQJCT16kqROgbmq87nCpqhO6U9sMVNbp901TDedjJDp7zSPIhQeR2TZdzCYdDmo0rjz-N2_ynUBMfxLDcSJg_oHCR3BdzH7C-ODW_U5YSmGcQnaGagYFhojeDZtVXg-Cmfu7S8gkA1JbhnBabtPYtNFNrUEsUqLpyQklC2pGj8WedgkGVOcze-zQOdGfM-C2y_g.IAvty3mOwv8cy2ie.JJClI0TU9rtrtvqz_AWZ_iY4ZrOOOLZuWNoIiwFdVHkz42xPunIx7lONaODL5Tz6yUhSQkENVe2TF9gBYfTHE9N1HKf0pBhkfXXuTOqD9HPyzD_dMUhrMOWOBa0JX99mBeTHwZx-NQbi4qAYrELmkZ8GUoaIWcp5FeDattoxrRPJkazsApp-zVMzjJLFM1UyFauinzWPuXDqVPqwfylVWDs8fzq3lu_tJmxOrctapiRbKOKE8CIDYt_njVtWQWKR8PiwbcpNMcEydc-Xy1Mg3OvYZ57RHgnkdkqnm-rfMsortiIrDd1d5tFnyL6nDmYXpVR31AsLnaaPEPHHRr8grLT25JtHqoyKmvy5arF2komkYzJPxD2vVqZRBXfqkZTKjotG8pWUrs9Q6BhYFIw34JM0GwTS2DDiTIeTG-ixYd0R51aSQCw9YIXAntYOq7ROEX5bjtanWYm-fttRVtL42iLbGZ2eJsr2fVvpfsBkVNZSmRNP0CH4jx4Zs42KEhA1IVbA6CiJLymrEPwoxtr13cU9GdkQrno8ukOw2EDtnPAZLhOCNpuF2wjw2QJFjr5MdQnPldpfDYoJNMmsYUhYOvcZzSf_SeUXCGJK0Fo7iJBpnDnXtReU0SK52WWjQi9hZDuuhVyQYAxsk4xrxPnS2LKxzXSzxEF_fAMO7KzIyL1aHqUezFyU7R0XrVNfRpp-TXoL6Kx0qDv5S4UklRau3WYuurRRQDeOwUS2-8j9dvGf45Iuy1IUa3POi0qdsPnjgB0KuYc0bRPxwIW8k-QDk-V4JbRhnpiO4np3Pvlv-mkaEOSM6clBJvZuVQ1P8-7mVGU3GW21vQvQX7nU4_jSnqjDhUWnQQQ9UhmEu5cBZz5cyLE9BAg_2wZVero-IJImapl0Q3yojG9C1mpGN9Bbj7Yh8-X7v3fVIwNX_nqzv3Hfmyzz7upfr0v8owrcCtMI37_0nrk4DwWKOCmWM-OgsDiyLMi4wWSxRqSeGtgmVNYbzchTDquuXweBoUnFJOOnx9XPpYpiG7I8f-Kzerj88vaC2U5-dcbn9_kfN8Rr197v5axR2UtjKFYCaI4ZuHEZoMJ92q2pLsSpWGA83CIOOok3IW44A8vuIdfQTUGMpv1A3GDt_fSVlJ12iNx5xK9-4UIizfx4UBm6zoyHq1Hs4qezQd5oQ2fYFjc1ieOBIrXJ0Z4qHQu3D1g8DHKkPKEVxyWBJk-kTMMl2HkN_N79rWZIH9rynX9H9JVnB5XjFkFYVcm71rq5tn7RkDrXgkFbLmr-ATTmZ4pu66v1qJJKVdwJ-vdAmMuG7kHOTSrFaUeFgPU-nbewFxdKEqiZd994hSGcHZpzXyoxqA.2YLIZ865tO-Qhjs8xO9mWA"

r_post = requests.post(f"https://api.jquants.com/v1/token/auth_refresh?refreshtoken={REFRESH_TOKEN}")
data = r_post.json()
idToken = data["idToken"]
headers = {'Authorization': 'Bearer {}'.format(idToken)}

# 銘柄コードを指定
code = "1925" 

# 財務情報の取得
statements = requests.get(f"https://api.jquants.com/v1/fins/statements?code={code}", headers=headers)
# pandasデータフレームに変換
df_statements = pd.DataFrame(statements.json()["statements"])

st.write("銘柄コード：" + code)
st.write(df_statements)

########################################################
#uploaded_file = "有価証券報告書（2022年3月期）.pdf"
#md_text = pymupdf4llm.to_markdown(uploaded_file)
#st.code(md_text, language='python')
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
