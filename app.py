import streamlit as st
from data_cleaning import clean_data
from analysis import generate_kpis
from alerts import check_alerts
from forecast import forecast_sales

st.set_page_config(page_title="AutoInsights", layout="wide")

st.title("AutoInsights Dashboard")

data = clean_data("train.csv")

total_sales, monthly_sales, category_sales, region_sales = generate_kpis(data)

# KPI Section
col1, col2 = st.columns(2)

with col1:
    st.metric("Total Sales", f"{total_sales:,.0f}")

with col2:
    alert = check_alerts(data)
    st.metric("Alert Status", alert)

# Charts
st.subheader("Sales by Category")
st.bar_chart(category_sales)

st.subheader("Sales by Region")
st.bar_chart(region_sales)

# Forecast
predictions = forecast_sales(data)
st.subheader("Next 7 Days Forecast")
st.line_chart(predictions)