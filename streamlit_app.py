import os
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pymupdf4llm
import yfinance as yf
from plotly import graph_objs as go
from plotly.offline import plot

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
ticker_symbol = "1925.T"
ticker_info = yf.Ticker(ticker_symbol)
df_bs=ticker_info.balance_sheet/1000000000 #貸借対照表
Total_Assets = df_bs.loc['Total Assets']  #総資産 #リストで格納
Current_Assets = df_bs.loc['Current Assets'] #流動資産
Total_Non_Current_Assets = df_bs.loc['Total Non Current Assets'] #固定資産合計
Current_Liabilities = df_bs.loc['Current Liabilities'] #流動負債
Total_Non_Current_Liabilities_Net_Minority_Interest = df_bs.loc['Total Non Current Liabilities Net Minority Interest']#非支配株主持分控除後固定負債合計
Total_Equity_Gross_Minority_Interest = df_bs.loc['Total Equity Gross Minority Interest']#非支配株主持分を含む総資本
labels = df_bs.columns.strftime('%Y年%m月%d日')
#np.array(assets)-np.array(liab)-np.array(equity)-np.array(minority)
# グラフ描画
fig1 = go.Figure(
   # データの指定
   data=[
        #go.Bar(
        #    name="総資産",
        #    x=labels,
        #    y=Total_Assets,
        #    offsetgroup=0,
        #),
        go.Bar(
            name="流動資産",
            x=labels,
            y=Current_Assets,
            base=Total_Non_Current_Assets,
            offsetgroup=0,
        ),
        go.Bar(
            name="固定資産",
            x=labels,
            y=Total_Non_Current_Assets,
            offsetgroup=0,
        ),
        go.Bar(
            name="流動負債",
            x=labels,
            y=Current_Liabilities,
            offsetgroup=1,
            base=Total_Non_Current_Liabilities_Net_Minority_Interest+Total_Equity_Gross_Minority_Interest,
        ),
       go.Bar(
            name="固定負債",
            x=labels,
            y=Total_Non_Current_Liabilities_Net_Minority_Interest,
            offsetgroup=1,
            base=Total_Equity_Gross_Minority_Interest,
        ),
        go.Bar(
            name="純資産",
            x=labels,
            y=Total_Equity_Gross_Minority_Interest,
            offsetgroup=1,
        ),
    ],
   # レイアウトの指定
    layout=go.Layout(
        title=ticker_symbol + " 貸借対照表(BS)",
        xaxis_title="決算期",
        yaxis_title="JPY(単位:十億円)"
    )
)
st.plotly_chart(fig1)
########################################################

# 大和ハウスの株価データを取得
ticker_symbol = "1925.T"
ticker_data = yf.Ticker(ticker_symbol)

# 過去1週間のデータを取得
#hist_data = ticker_data.history(period="1wk")

# 取得したデータを表示
#st.write(hist_data)

ticker_info = yf.Ticker(ticker_symbol)

# 貸借対照表
def show_balance_sheet_item(item):
    if item in balance_sheet.index:
        item_data = balance_sheet.loc[item]
        st.write(f"\n--- " + item + " for " + ticker_symbol + " ---")
        st.write(item_data)

#show_balance_sheet_item("Working Capital")
#######################################
def balance_sheet_outline(ticker_symbol):
    ticker_info = yf.Ticker(ticker_symbol)
    balance_sheet = ticker_info.balance_sheet/1000000000 #年単位（10億円単位）
    #balance_sheet = ticker_info.quarterly_balance_sheet/1000000000 #4ヶ月単位（10億円単位）
    balance_sheet.columns = balance_sheet.columns[::-1]

    def balance_sheet_items(item):
        if item in balance_sheet.index:
            item_data = balance_sheet.loc[item]
            return item_data
    
    Total_Assets =balance_sheet_items("Total Assets") #総資産
    Current_Assets =balance_sheet_items("Current Assets") #流動資産
    Total_Non_Current_Assets =balance_sheet_items("Total Non Current Assets") #固定資産合計
    Current_Liabilities =balance_sheet_items("Current Liabilities") #流動負債
    Total_Non_Current_Liabilities_Net_Minority_Interest =balance_sheet_items("Total Non Current Liabilities Net Minority Interest") #非支配株主持分控除後固定負債合計
    Total_Equity_Gross_Minority_Interest =balance_sheet_items("Total Equity Gross Minority Interest") #非支配株主持分を含む総資本
    return pd.concat([Total_Assets,Current_Assets,Total_Non_Current_Assets,Current_Liabilities,Total_Non_Current_Liabilities_Net_Minority_Interest,Total_Equity_Gross_Minority_Interest], axis=1) # axis=1 で列方向に結合
#######################################

# 損益計算書
#######################################
def income_stmt_outline(ticker_symbol):
    ticker_info = yf.Ticker(ticker_symbol)
    income_stmt = ticker_info.income_stmt/1000000000 #年単位（10億円単位）
    #income_stmt = ticker_info.quarterly_income_stmt/1000000000 #4ヶ月単位（10億円単位）
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

# キャッシュフロー
#######################################
def Cash_Flow_outline(ticker_symbol):
    ticker_info = yf.Ticker(ticker_symbol)
    Cash_Flow = ticker_info.cash_flow/1000000000 #年単位（10億円単位）
    #Cash_Flow = ticker_info.quarterly_cash_flow/1000000000 #4ヶ月単位（10億円単位）
    Cash_Flow.columns = Cash_Flow.columns[::-1]

    def Cash_Flow_outline_items(item):
        if item in Cash_Flow.index:
            item_data = Cash_Flow.loc[item]
            return item_data
    
    Operating_CF =Cash_Flow_outline_items("Operating Cash Flow")
    Investing_CF =Cash_Flow_outline_items("Investing Cash Flow")
    Free_CF =Cash_Flow_outline_items("Free Cash Flow")
    Financing_CF =Cash_Flow_outline_items("Financing Cash Flow")
    return pd.concat([Operating_CF, Investing_CF, Free_CF, Financing_CF], axis=1) # axis=1 で列方向に結合
#######################################



col1, col2 = st.columns([2, 2],border=True)
with col1:
    ticker_symbol = "1925.T"
    st.subheader(ticker_symbol + ": " + yf.Ticker(ticker_symbol).info["longName"])
    st.divider()
    # 損益計算書
    st.subheader("Income Statement (Bil. JPY)")
    df_output = income_stmt_outline(ticker_symbol)
    st.write(df_output.T)
    st.line_chart(df_output)
    #st.write(df_output.index.values) # 行名取得
    #st.write(df_output.columns.values) # 列名取得
    st.bar_chart(df_output.T.head(), stack=False)    
    st.divider()
    # キャッシュフロー
    st.subheader("Cash Flow (Bil. JPY)")
    df_output = Cash_Flow_outline(ticker_symbol)
    st.write(df_output.T)
    st.line_chart(df_output) 
    st.divider()
    # 貸借対照表
    st.subheader("Balance Sheet (Bil. JPY)")
    df_output = balance_sheet_outline(ticker_symbol)
    st.write(df_output.T)

with col2:
    ticker_symbol = "1928.T"
    st.subheader(ticker_symbol + ": " + yf.Ticker(ticker_symbol).info["longName"])
    st.divider()
    # 損益計算書
    st.subheader("Income Statement (Bil. JPY)")
    df_output = income_stmt_outline(ticker_symbol)
    st.write(df_output.T)
    st.line_chart(df_output)
    st.bar_chart(df_output.T.head(), stack=False)
    st.divider()
    # キャッシュフロー
    st.subheader("Cash Flow (Bil. JPY)")
    df_output = Cash_Flow_outline(ticker_symbol)
    st.write(df_output.T)
    st.line_chart(df_output) 
    st.divider()
    # 貸借対照表
    st.subheader("Balance Sheet (Bil. JPY)")
    df_output = balance_sheet_outline(ticker_symbol)
    st.write(df_output.T)

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
