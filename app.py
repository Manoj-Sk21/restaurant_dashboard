import pandas as pd
import streamlit as st
df=pd.read_csv("Zomato.csv")
st.set_page_config(layout="wide")
st.title("My fist real world app")
all_area=df['Area'].unique()
selected_area=st.selectbox("select the Area",all_area)
filterd_df=df[df['Area']==selected_area]
all_cuisine=filterd_df['Cuisines'].unique()
selected_cuisine=st.selectbox("select the cuisine",all_cuisine)
final_df=filterd_df[filterd_df['Cuisines']==selected_cuisine]
st.bar_chart(final_df['AverageCost'])
st.dataframe(final_df)