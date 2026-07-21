import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
st.title("FAANG Stock Price Prediction")

st.write("Predict the closing stock price.")
open_price = st.number_input("Open Price")

volume = st.number_input("Volume")

company = st.selectbox(
    "Company",
    ["Amazon","Apple","Facebook","Google","Netflix"]
)

year = st.number_input("Year")


month = st.number_input("Month")

day = st.number_input("Day")
company_dict = {
    "Amazon":0,
    "Apple":1,
    "Facebook":2,
    "Google":3,
    "Netflix":4
}

company = company_dict[company]
new_data = pd.DataFrame({

    "Open":[open_price],
    "Volume":[volume],
    "Company":[company],
    "Year":[year],
    "Month":[month],
    "Day":[day]

})
new_data = scaler.transform(new_data)
prediction = model.predict(new_data)
if st.button("Predict"):

    prediction = model.predict(new_data)

    st.success(f"Predicted Close Price : {prediction[0]:.2f}")