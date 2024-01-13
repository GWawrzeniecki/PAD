import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Plotting Demo", page_icon="📈")

st.markdown("# Wizualizacja rozkładu zmiennych")

st.write(
    """Opis """
)

data = pd.read_csv('pad/Projekt/prepared_data.csv')

# Rozkład zmiennych
column_name = st.selectbox("Rozkład", ("carat", "table", "depth"))
fig1 = px.histogram(data, x=column_name, color=column_name, title='Rozkład zmiennych')
st.plotly_chart(fig1, use_container_width=True)

# Zależność ceny od zmiennych
column_name = st.selectbox("Zależność ceny od zmiennych", ("carat", "table", "depth"))
fig1 = px.scatter(data, x=column_name, y='price', trendline='ols', title='Zależność ceny od zaznaczonej zmiennej')
st.plotly_chart(fig1, use_container_width=True)

# Zależność ceny od zmiennych kategorycznych
column_name = st.selectbox("Zależność ceny od zmiennych kategorycznych", ("clarity", "color", "cut"))
fig1 = px.box(data, x=column_name, y='price', color=column_name, title='Zależność od zmiennej kategorycznej')
st.plotly_chart(fig1, use_container_width=True)

# Liczebność kategorii
column_name = st.selectbox("Liczebność kategorii", ("clarity", "color", "cut"))
category_counts = data[column_name].value_counts()
fig1 = px.bar(x=category_counts.index, y=category_counts.values, color=category_counts.index, title='Liczebność kategorii', labels={'x': 'Kategoria', 'y': 'Liczebność'})
st.plotly_chart(fig1, use_container_width=True)

# Rozkład kategorii
category_counts = data[column_name].value_counts()
fig1 = px.pie(names=category_counts.index, values=category_counts.values, title='Rozkład kategorii')
st.plotly_chart(fig1, use_container_width=True)
