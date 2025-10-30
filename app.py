import pandas as pd
import streamlit as st
df=pd.read_csv("Zomato.csv")
st.set_page_config(layout="wide")
st.title("My fist real world app")
all_area=df['Area'].unique()
selected_area=st.selectbox("select the Area",all_area)
filterd_df=df[df['Area']==selected_area]
st.dataframe(filterd_df)