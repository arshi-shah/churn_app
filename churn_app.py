"""
===============================
Customer Churn Prediction App (Streamlit)
===============================
This app loads a trained model and encoders, takes user input, and predicts customer churn.

Follow the TODOs and fill in the blanks (____) to complete the app!
"""

import streamlit as st
from joblib import load
import pandas as pd
import json

model_filepath = './models/random_forest_model_v1.joblib'
internet_service_encoder_filepath = './models/internet_service_encoder.joblib'
contract_encoder_filepath = './models/contract_encoder.joblib'
labels_filepath = './models/feature_labels.json'


# 1. Import required libraries
import streamlit as st
# TODO: Import load from joblib
from joblib import load
import pandas as pd
import json

# 2. Define file paths
model_filepath = './models/random_forest_model_v1.joblib'
internet_service_encoder_filepath = './models/internet_service_encoder.joblib'
contract_encoder_filepath = './models/contract_encoder.joblib'
labels_filepath = './models/feature_labels.json'

# 3. Load the trained model and encoders

# TODO: Load the model using joblib's load function
model = load(model_filepath)

# TODO: Load the encoders for InternetService and Contract
internet_service_encoder = load(internet_service_encoder_filepath)
contract_encoder = load(contract_encoder_filepath)

# Load feature labels for dropdowns
with open(labels_filepath, 'r') as f:
    feature_labels = json.load(f)

# Create a Streamlit app
st.title("Customer Churn Prediction App")

# Input fields for feature values on the main screen
st.header("Enter Customer Information")
tenure = st.number_input("Tenure (in months)", min_value=0, max_value=100, value=1)
internet_service = st.selectbox("Internet Service", feature_labels['InternetService'])
contract = st.selectbox("Contract", feature_labels['Contract'])
monthly_charges = st.number_input("Monthly Charges", min_value=0, max_value=200, value=50)
total_charges = st.number_input("Total Charges", min_value=0, max_value=10000, value=0)

# Use the correct encoder to transform input values

# 5. Encode categorical inputs
# TODO: Use the encoders to transform the selected values
internet_service_encoded = internet_service_encoder.transform([internet_service])[0]  # TODO: Fill this
contract_encoded = contract_encoder.transform([contract])[0]  # TODO: Fill this

# Prepare input as a DataFrame with correct feature names
input_df = pd.DataFrame([{
    'tenure': tenure,
    'InternetService': internet_service_encoded,
    'Contract': contract_encoded,
    'MonthlyCharges': monthly_charges,
    'TotalCharges': total_charges
}])

# Make a prediction using the model

# 7. Make a prediction using the model
# TODO: Use the model to predict churn (0 = stay, 1 = churn)
prediction = model.predict(input_df)  # TODO: Fill this

# Display the prediction result on the main screen
st.header("Prediction Result")
if prediction[0] == 0:
    st.success("This customer is likely to stay.")
else:
    st.error("This customer is likely to churn.")
