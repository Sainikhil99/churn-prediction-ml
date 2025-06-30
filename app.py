import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('models/churn_model.pkl')

# App title
st.title("💼 Customer Churn Prediction App")

# User Inputs
st.header("📋 Enter Customer Details")

gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen", [0, 1])
tenure = st.slider("Tenure (months)", 0, 72)
monthly_charges = st.number_input("Monthly Charges", 0.0, 200.0)
total_charges = st.number_input("Total Charges", 0.0, 10000.0)

# Convert categorical input
gender = 1 if gender == "Male" else 0

# Combine input
input_data = np.array([[gender, senior, tenure, monthly_charges, total_charges]])

# Predict button
if st.button("Predict Churn"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error("⚠️ Customer is likely to Churn!")
    else:
        st.success("✅ Customer is likely to Stay.")
