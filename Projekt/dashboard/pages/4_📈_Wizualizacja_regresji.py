import statsmodels.formula.api as smf
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
import pandas as pd

st.markdown("# Wizualizacja modelu regresji")

data = pd.read_csv('Projekt/prepared_data.csv')
model = smf.ols("price ~ carat + clarity", data=data).fit()

data["fitted"] = model.fittedvalues

fig = go.Figure()
# Note that we still plot against the original Year variable
fig.add_trace(go.Scatter(
    x=data["carat"], y=data["price"], name="Year vs Sea Ice Extent (million sq km)", mode="markers"))
fig.add_trace(go.Scatter(
    x=data["carat"], y=data["fitted"], name="Fitted Regression Line"))
fig.update_layout(title="Regression line of Year vs Sea Ice Extent (million sq km)", xaxis_title="Year",
    yaxis_title="Sea Ice Extent")

st.plotly_chart(fig, use_container_width=True)

# # Create a scatter plot with different colors for each clarity level
# fig = px.scatter(data, x="carat", y="price", color="clarity")
#
# # Add the regression line
# fig.add_trace(go.Scatter(x=data["carat"], y=data["fitted"], name="Fitted Regression Line", mode="lines"))
#
# # Update the layout with appropriate titles
# fig.update_layout(title="Price vs Carat Size by Clarity Level",
#                   xaxis_title="carat",
#                   yaxis_title="price")
#
# st.plotly_chart(fig, use_container_width=True)
