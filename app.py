import streamlit as st
import pandas as pd
import joblib

# Load model, encoder, and features list
model = joblib.load('models/churn_model.pkl')
model_features = joblib.load('models/features.pkl')  # all one-hot and numeric features

st.title("A Customer Churn Prediction App")
st.subheader("📋 Enter Customer Details")

# User inputs
gender = st.selectbox("Gender", ["Male", "Female"])
senior_citizen = st.selectbox("Senior Citizen", [0, 1])
tenure = st.slider("Tenure (months)", 0, 72, 1)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, step=0.01)
total_charges = st.number_input("Total Charges", min_value=0.0, step=0.01)
partner = st.selectbox("Partner", ["Yes", "No"])

if st.button("Predict Churn"):
    # Initialize input dataframe with zeros for all features
    input_data = pd.DataFrame(columns=model_features)
    input_data.loc[0] = 0

    # Fill numerical features
    input_data.at[0, 'seniorcitizen'] = senior_citizen
    input_data.at[0, 'tenure'] = tenure
    input_data.at[0, 'monthlycharges'] = monthly_charges
    input_data.at[0, 'totalcharges'] = total_charges

    # Fill one-hot encoded features based on user inputs
    # For gender
    gender_col = f"gender_{gender.lower()}"
    if gender_col in input_data.columns:
        input_data.at[0, gender_col] = 1

    # For partner
    partner_col = f"partner_{partner.lower()}"
    if partner_col in input_data.columns:
        input_data.at[0, partner_col] = 1

    # Add other categorical features similarly...

    # Debug info
    st.write("🔎 Input data passed to model:")
    st.write(input_data)

    # Predict
    try:
        prediction = model.predict(input_data)[0]
        proba = model.predict_proba(input_data)[0][1]
    except Exception as e:
        st.error(f"Prediction error: {e}")
        st.stop()

    # Show result
    if prediction == 1:
        st.error(f"⚠️ The customer is likely to churn with probability {proba:.2%}")
    else:
        st.success(f"✅ The customer is NOT likely to churn with probability {1 - proba:.2%}")
