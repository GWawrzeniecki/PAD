import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Jewellery",
    page_icon="💎",
)

st.title("Wyroby złote - Analiza zbioru danych")
st.header('PAD')
st.subheader('Grzegorz Wawrzeniecki')

data = pd.read_csv('prepared_data.csv')
st.dataframe(data.head(10))
