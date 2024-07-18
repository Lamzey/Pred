import streamlit as st
from sales_prediction import sales_prediction

# Call the functions to get the data and forecasts
sales_prediction_result = sales_prediction()

# Display the data and forecasts
st.title('My Data Dashboard')

st.header('Sales & Revenue Prediction')
st.write(sales_prediction_result)