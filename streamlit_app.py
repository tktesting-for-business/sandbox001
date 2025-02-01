import streamlit as st
import july
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

url = 'https://docs.google.com/spreadsheets/'

# Set up API credentials and open the worksheet
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'cred.json', scope)
gc = gspread.authorize(credentials)
workbook = gc.open_by_url(url)
worksheet = workbook.worksheet('Sheet1')

data = worksheet.get_all_values()
headers = data.pop(0)

df = pd.DataFrame(data, columns=headers)

df['Dates'] = pd.to_datetime(df.Dates)
df['Dates'] = df['Dates'].dt.strftime('%Y-%m-%d')

july.heatmap(dates=df.Dates,
                       data=df.Pages,
                       cmap='github',
                       month_grid=True,
                       horizontal=True,
                       value_label=True,
                       date_label=False,
                       weekday_label=True,
                       month_label=True,
                       year_label=True,
                       colorbar=True,
                       fontfamily="monospace",
                       fontsize=12,
                       title="Daily Pages Read")
