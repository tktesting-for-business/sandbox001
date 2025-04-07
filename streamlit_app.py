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

# 複数選択ボックスのオプションを定義
#######################################
options = ['1925.T:大和ハウス', '1928.T:積水ハウス', '2685.T:アダストリア','8016.T:オンワード']

# レイアウト
#######################################
st.set_page_config(layout="wide")
st.title("Analyzing financial statements")
st.write("This is a testing site with yfinance API")
with st.sidebar:
    st.title("sidebar title")
    st.button("hello")
    st.text("hello world")
    st.divider()
    st.radio("Views",["Overview","Detail of income statement","Detail of cash flow"])


# 複数選択ボックスを作成し、ユーザーの選択を取得
choice = st.multiselect('企業を２つ選んでください',
            options,
            options[:2],
            max_selections = 2,
            placeholder="選んでください")

# ユーザーの選択に応じたメッセージを表示
try
    st.write(f'あなたが選んだのは{"、".join(choice)}です。')
    target = ':'
    idx = choice[0].find(target)
    r = choice[0][:idx] 
    st.write(r)
except (TypeError) as e:
    st.write(e)
    
col1, col2 = st.columns([2, 2],border=True)

# 貸借対照表
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
    Working_Capital = balance_sheet_items("Working Capital") #Working Capital    
    return pd.concat([Total_Assets,Current_Assets,Total_Non_Current_Assets,Current_Liabilities,Total_Non_Current_Liabilities_Net_Minority_Interest,Total_Equity_Gross_Minority_Interest,Working_Capital], axis=1) # axis=1 で列方向に結合

# 貸借対照表グラフ
#######################################
def balance_sheet_graph(ticker_symbol):
    ticker_info = yf.Ticker(ticker_symbol)
    balance_sheet = ticker_info.balance_sheet/1000000000 #年単位（10億円単位）
    #balance_sheet = ticker_info.quarterly_balance_sheet/1000000000 #4ヶ月単位（10億円単位）
    balance_sheet.columns = balance_sheet.columns[::-1]
    Total_Assets = balance_sheet.loc['Total Assets']  #総資産 #リストで格納
    Current_Assets = balance_sheet.loc['Current Assets'] #流動資産
    Total_Non_Current_Assets = balance_sheet.loc['Total Non Current Assets'] #固定資産合計
    Current_Liabilities = balance_sheet.loc['Current Liabilities'] #流動負債
    Total_Non_Current_Liabilities_Net_Minority_Interest = balance_sheet.loc['Total Non Current Liabilities Net Minority Interest']#非支配株主持分控除後固定負債合計
    Total_Equity_Gross_Minority_Interest = balance_sheet.loc['Total Equity Gross Minority Interest']#非支配株主持分を含む総資本
    labels = balance_sheet.columns.strftime('%Y-%m-%d')
    # グラフ描画
    fig1 = go.Figure(
       # データの指定
       data=[
            go.Bar(
                name="Current Assets",
                x=labels,
                y=Current_Assets,
                base=Total_Non_Current_Assets,
                offsetgroup=0,
            ),
            go.Bar(
                name="Fixed Assets",
                x=labels,
                y=Total_Non_Current_Assets,
                offsetgroup=0,
            ),
            go.Bar(
                name="Current Liabilities",
                x=labels,
                y=Current_Liabilities,
                offsetgroup=1,
                base=Total_Non_Current_Liabilities_Net_Minority_Interest+Total_Equity_Gross_Minority_Interest,
            ),
           go.Bar(
                name="Non Current Liabilitie",
                x=labels,
                y=Total_Non_Current_Liabilities_Net_Minority_Interest,
                offsetgroup=1,
                base=Total_Equity_Gross_Minority_Interest,
            ),
            go.Bar(
                name="Net Asset",
                x=labels,
                y=Total_Equity_Gross_Minority_Interest,
                offsetgroup=1,
            ),
        ],
       # レイアウトの指定
        layout=go.Layout(
            #title="Balance Sheet",
            xaxis_title="Fiscal year end",
            yaxis_title="JPY (Bil.)"
        )
    )
    st.plotly_chart(fig1)


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

# Financial Contents View
#######################################
def financial_contents_view(ticker_symbol):
    st.subheader(ticker_symbol + ": " + yf.Ticker(ticker_symbol).info["longName"])
    st.write("Industry: " + yf.Ticker(ticker_symbol).info["industry"])    
    st.write("Sector: " + yf.Ticker(ticker_symbol).info["sector"])
    
    st.divider()
    # 損益計算書
    st.subheader("Income Statement (Bil. JPY)")
    df_output_Income = income_stmt_outline(ticker_symbol)
    st.write(df_output_Income.T)
    df_output_Income.index = df_output_Income.index.strftime('%Y-%m-%d')
    st.line_chart(df_output_Income)
    #st.bar_chart(df_output_Income.T.head(), stack=False) 
    st.divider()
    # キャッシュフロー
    st.subheader("Cash Flow (Bil. JPY)")
    df_output_CF = Cash_Flow_outline(ticker_symbol)
    st.write(df_output_CF.T)
    df_output_CF.index = df_output_CF.index.strftime('%Y-%m-%d')    
    st.line_chart(df_output_CF) 
    st.divider()
    # 貸借対照表
    st.subheader("Balance Sheet (Bil. JPY)")
    df_output_BS = balance_sheet_outline(ticker_symbol)
    df_output_BS.index = df_output_BS.index.strftime('%Y-%m-%d')
    st.write(df_output_BS.T)
    balance_sheet_graph(ticker_symbol)
    st.write('Working Capital')
    st.line_chart(df_output_BS.T.loc['Working Capital'])
    st.divider()
    # 比率分析
    st.subheader('ROA：Net Income/Total Assets (Bil. JPY)')
    st.line_chart(df_output_Income.T.loc['Net Income']/df_output_BS.T.loc['Total Assets'])

# コンテンツ表示（2列）
#######################################
#"1925.T"#大和ハウス
#"1928.T"#積水ハウス
#"2685.T"#アダストリア
#"8016.T"#オンワード

with col1:
    financial_contents_view("1925.T")
with col2:
    financial_contents_view("1928.T")
    
# 配当金
#dividends = ticker_info.dividends

# 決算日
#earnings_dates = ticker_info.earnings_dates

# 財務諸表
#financials = ticker_info.financials
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
