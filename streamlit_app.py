import os
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pymupdf4llm

########################################################
import requests
import json

REFRESH_TOKEN = "eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.GVCUJEhqSvCE_WRCOqSOgj6Dvu1oY0Oqd36JEexRVkKASxZbIljwauEnNl4zYWhIkSfd1EXkOZzEh8SHT0IldNYbV9Nnk0YJhN3rwzo5YEciDhBQ-sD3raV9woHDbEAcfOcgbddTUJ2-shH-E_boQJCT16kqROgbmq87nCpqhO6U9sMVNbp901TDedjJDp7zSPIhQeR2TZdzCYdDmo0rjz-N2_ynUBMfxLDcSJg_oHCR3BdzH7C-ODW_U5YSmGcQnaGagYFhojeDZtVXg-Cmfu7S8gkA1JbhnBabtPYtNFNrUEsUqLpyQklC2pGj8WedgkGVOcze-zQOdGfM-C2y_g.IAvty3mOwv8cy2ie.JJClI0TU9rtrtvqz_AWZ_iY4ZrOOOLZuWNoIiwFdVHkz42xPunIx7lONaODL5Tz6yUhSQkENVe2TF9gBYfTHE9N1HKf0pBhkfXXuTOqD9HPyzD_dMUhrMOWOBa0JX99mBeTHwZx-NQbi4qAYrELmkZ8GUoaIWcp5FeDattoxrRPJkazsApp-zVMzjJLFM1UyFauinzWPuXDqVPqwfylVWDs8fzq3lu_tJmxOrctapiRbKOKE8CIDYt_njVtWQWKR8PiwbcpNMcEydc-Xy1Mg3OvYZ57RHgnkdkqnm-rfMsortiIrDd1d5tFnyL6nDmYXpVR31AsLnaaPEPHHRr8grLT25JtHqoyKmvy5arF2komkYzJPxD2vVqZRBXfqkZTKjotG8pWUrs9Q6BhYFIw34JM0GwTS2DDiTIeTG-ixYd0R51aSQCw9YIXAntYOq7ROEX5bjtanWYm-fttRVtL42iLbGZ2eJsr2fVvpfsBkVNZSmRNP0CH4jx4Zs42KEhA1IVbA6CiJLymrEPwoxtr13cU9GdkQrno8ukOw2EDtnPAZLhOCNpuF2wjw2QJFjr5MdQnPldpfDYoJNMmsYUhYOvcZzSf_SeUXCGJK0Fo7iJBpnDnXtReU0SK52WWjQi9hZDuuhVyQYAxsk4xrxPnS2LKxzXSzxEF_fAMO7KzIyL1aHqUezFyU7R0XrVNfRpp-TXoL6Kx0qDv5S4UklRau3WYuurRRQDeOwUS2-8j9dvGf45Iuy1IUa3POi0qdsPnjgB0KuYc0bRPxwIW8k-QDk-V4JbRhnpiO4np3Pvlv-mkaEOSM6clBJvZuVQ1P8-7mVGU3GW21vQvQX7nU4_jSnqjDhUWnQQQ9UhmEu5cBZz5cyLE9BAg_2wZVero-IJImapl0Q3yojG9C1mpGN9Bbj7Yh8-X7v3fVIwNX_nqzv3Hfmyzz7upfr0v8owrcCtMI37_0nrk4DwWKOCmWM-OgsDiyLMi4wWSxRqSeGtgmVNYbzchTDquuXweBoUnFJOOnx9XPpYpiG7I8f-Kzerj88vaC2U5-dcbn9_kfN8Rr197v5axR2UtjKFYCaI4ZuHEZoMJ92q2pLsSpWGA83CIOOok3IW44A8vuIdfQTUGMpv1A3GDt_fSVlJ12iNx5xK9-4UIizfx4UBm6zoyHq1Hs4qezQd5oQ2fYFjc1ieOBIrXJ0Z4qHQu3D1g8DHKkPKEVxyWBJk-kTMMl2HkN_N79rWZIH9rynX9H9JVnB5XjFkFYVcm71rq5tn7RkDrXgkFbLmr-ATTmZ4pu66v1qJJKVdwJ-vdAmMuG7kHOTSrFaUeFgPU-nbewFxdKEqiZd994hSGcHZpzXyoxqA.2YLIZ865tO-Qhjs8xO9mWA"

r_post = requests.post(f"https://api.jquants.com/v1/token/auth_refresh?refreshtoken={REFRESH_TOKEN}")
data = r_post.json()
idToken = data["idToken"]

headers = {'Authorization': 'Bearer {}'.format(idToken)}

# 銘柄コード、期間を指定
code_ = "19250" 
from_ = "2024-12-01"
to_ = "2025-01-01"


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
