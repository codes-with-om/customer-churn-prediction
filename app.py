import streamlit as st
import numpy as np
import joblib

# load model
model = joblib.load('churn_model.pkl')
scaler = joblib.load('scaler.pkl')

st.set_page_config(page_title="Churn Predictor", page_icon="📊")

st.title("📊 Customer Churn Prediction")
st.markdown("### Enter customer details below:")

# layout (2 columns)
col1, col2 = st.columns(2)

with col1:
    tenure = st.number_input("Tenure (months)", min_value=0)
    contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])

with col2:
    monthly_charges = st.number_input("Monthly Charges")
    internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

# encoding
contract_one_year = 1 if contract == "One year" else 0
contract_two_year = 1 if contract == "Two year" else 0

internet_fiber = 1 if internet == "Fiber optic" else 0
internet_no = 1 if internet == "No" else 0

if st.button("🔍 Predict"):

    input_data = np.array([[
        tenure,
        monthly_charges,
        contract_one_year,
        contract_two_year,
        internet_fiber,
        internet_no
    ]])

    input_scaled = scaler.transform(input_data)

    prob = model.predict_proba(input_scaled)[0][1]

    if prob > 0.4:
        st.error(f"⚠️ High Churn Risk ({prob:.2f})")
    else:
        st.success(f"✅ Low Churn Risk ({prob:.2f})")