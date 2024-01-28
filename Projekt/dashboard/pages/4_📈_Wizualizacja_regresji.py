import pandas as pd
import plotly.graph_objects as go
import statsmodels.formula.api as smf
import streamlit as st

st.markdown("# Wizualizacja modelu regresji")

data = pd.read_csv('Projekt/prepared_data.csv')

clarity = st.selectbox("Regresja liniowa ", data['clarity'].unique())
subset = data[data['clarity'] == clarity]

fig = go.Figure()

fig.add_trace(go.Scatter(x=subset["carat"], y=subset["price"], name="Carat vs Price", mode="markers"))

fitted_values = smf.ols("price ~ carat", data=subset).fit().fittedvalues # wartości przewidziane
fig.add_trace(go.Scatter(x=subset["carat"], y=fitted_values, mode='lines', name=f'Fitted - {clarity}'))

fig.update_layout(title="Regresja liniowa zależność wzrostu cen od wielkości caratu i czystości wyrobu", xaxis_title="Carat", yaxis_title="Price")

st.plotly_chart(fig, use_container_width=True)
