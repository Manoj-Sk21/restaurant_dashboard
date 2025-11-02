import pandas as pd
import streamlit as st
import requests
# df=pd.read_csv("Zomato.csv")
st.set_page_config(layout="wide")
st.title("Full stack dashboard")
API_URL = "https://web-production-b127d.up.railway.app/api/jobs"
@st.cache_data
def load_data(url):
    response = requests.get(url)
    data = response.json()
    return pd.DataFrame(data)
df = load_data(API_URL)
all_area=df['Area'].unique()
selected_area=st.selectbox("select the Area",all_area)
filterd_df=df[df['Area']==selected_area]
all_cuisine=filterd_df['Cuisines'].unique()
selected_cuisine=st.selectbox("select the cuisine",all_cuisine)
final_df=filterd_df[filterd_df['Cuisines']==selected_cuisine]
st.bar_chart(final_df['AverageCost'])
st.dataframe(final_df)