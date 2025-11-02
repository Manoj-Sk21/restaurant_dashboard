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
all_location=df['location'].unique()
selected_location=st.selectbox("select the location",all_location)
filterd_df=df[df['location']==selected_location]
all_title=filterd_df['title'].unique()
selected_title=st.selectbox("select the title",all_title)
final_df=filterd_df[filterd_df['title']==selected_title]
# st.bar_chart(final_df['AverageCost'])
st.dataframe(final_df)