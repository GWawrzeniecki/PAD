import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Jewellery",
    page_icon="💎",
)

# st.title("Analiza zbioru danych")
# st.header("PAD")
#
# st.markdown("# Wyroby złote - próbka danych")
# data = pd.read_csv('messy_data.csv')
# st.dataframe(data.head(20), hide_index=True)
#
# st.subheader('Grzegorz Wawrzeniecki')



st.markdown("# Analiza zbioru danych")
st.markdown("## PAD")

st.markdown("## Wyroby złote - próbka danych")
data = pd.read_csv('Projekt/messy_data.csv')
st.dataframe(data.head(20), hide_index=True)

st.markdown('## Grzegorz Wawrzeniecki')