import os
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pymupdf4llm
import altair as alt

#import sandbox_app

st.set_page_config(layout="wide")
st.title("Analyzing financial statements")
st.write("This is a testing site with yfinance API")
with st.sidebar:
    st.title("sidebar title")
    st.button("hello")
    st.text("hello world")
    st.divider()
    st.radio("fruits",["apple","orange","melon"])
    
########################################################
import yfinance as yf
from streamlit.column_config import BarChartColumn

# 大和ハウスの株価データを取得
ticker_symbol = "1925.T"
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
#######################################
def income_stmt_outline(ticker_symbol):
    ticker_info = yf.Ticker(ticker_symbol)
    income_stmt = ticker_info.income_stmt #年単位
    #income_stmt = ticker_info.quarterly_income_stmt #4ヶ月単位
    income_stmt.columns = income_stmt.columns[::-1]

    def income_stmt_items(item):
        if item in income_stmt.index:
            item_data = income_stmt.loc[item]
            return item_data
    
    Total_Revenue =income_stmt_items("Total Revenue")
    Gross_Profit =income_stmt_items("Gross Profit")
    Operating_Income =income_stmt_items("Operating Income")
    Pretax_Income =income_stmt_items("Pretax Income")
    Net_Income =income_stmt_items("Net Income")
    return pd.concat([Total_Revenue, Gross_Profit,Operating_Income,Pretax_Income,Net_Income], axis=1) # axis=1 で列方向に結合
#######################################

col1, col2 = st.columns([2, 2],border=True)
with col1:
    ticker_symbol = "1925.T"
    st.header(ticker_symbol + ": " + yf.Ticker(ticker_symbol).info["longName"])
    # 損益計算書
    st.subheader("Income Statement")
    df_output = income_stmt_outline(ticker_symbol)
    st.write(df_output.T)
    st.line_chart(df_output)
    #st.altair_chart(df_output)
    #st.dataframe(df_output, column_config=column_config) # データフレームを表示
    st.divider()
    # キャッシュフロー
    st.subheader("Cash Flow")
    ticker_info = yf.Ticker(ticker_symbol)
    cash_flow = ticker_info.cash_flow
    cash_flow.columns = cash_flow.columns[::-1]
    st.write(cash_flow)
    st.divider()
    # 貸借対照表
    st.subheader("Balance Sheet")
    ticker_info = yf.Ticker(ticker_symbol)
    balance_sheet = ticker_info.balance_sheet
    balance_sheet.columns = balance_sheet.columns[::-1]
    st.write(balance_sheet)

with col2:
    ticker_symbol = "1928.T"
    st.header(ticker_symbol + ": " + yf.Ticker(ticker_symbol).info["longName"])
    # 損益計算書
    st.subheader("Income Statement")
    df_output = income_stmt_outline(ticker_symbol)
    st.write(df_output.T)
    st.line_chart(df_output)
    st.divider()
    # キャッシュフロー
    st.subheader("Cash Flow")
    ticker_info = yf.Ticker(ticker_symbol)
    cash_flow = ticker_info.cash_flow
    cash_flow.columns = cash_flow.columns[::-1]
    st.write(cash_flow)
    st.divider()
    # 貸借対照表
    st.subheader("Balance Sheet")
    ticker_info = yf.Ticker(ticker_symbol)
    balance_sheet = ticker_info.balance_sheet
    balance_sheet.columns = balance_sheet.columns[::-1]
    st.write(balance_sheet)


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
