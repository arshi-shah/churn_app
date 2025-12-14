# ===============================
# Customer Churn Model Training Script
# ===============================
# This script loads the telecom churn dataset, preprocesses it, trains a Random Forest model,
# and saves the model and encoders for later use in the app.
#
# Follow the TODOs and fill in the blanks (____) to complete the script!

# 1. Import required libraries
import pandas as pd
# TODO: Import RandomForestClassifier from sklearn.ensemble
from sklearn.ensemble import RandomForestClassifier  # TODO: Fill this
# TODO: Import LabelEncoder from sklearn.preprocessing
from sklearn.preprocessing import LabelEncoder  # TODO: Fill this
from joblib import dump
import json

# 2. Define file paths
data_filepath = './data/Telecom_Customer_Churn.csv'
model_filepath = './models/random_forest_model_v1.joblib'

# 3. Load the dataset
# TODO: Load the CSV file into a pandas DataFrame
telecom_customer_data = pd.read_csv(data_filepath)  # TODO: Fill this

# 4. Data preprocessing
# Convert 'TotalCharges' to numeric and fill missing values
telecom_customer_data['TotalCharges'] = pd.to_numeric(telecom_customer_data['TotalCharges'], errors='coerce')
telecom_customer_data['TotalCharges'] = telecom_customer_data['TotalCharges'].fillna(0)

# 5. Encode categorical variables
# We need to convert categorical columns to numbers for the model
# TODO: Create LabelEncoders for 'Churn', 'InternetService', and 'Contract'
churn_encoder = LabelEncoder()  # TODO: Fill this
internet_service_encoder = LabelEncoder()  # TODO: Fill this
contract_encoder = LabelEncoder()  # TODO: Fill this

# TODO: Fit and transform the encoders on the respective columns
# telecom_customer_data['Churn'] = churn_encoder.fit_transform('Churn')  # TODO: Fill this
# telecom_customer_data['InternetService'] = internet_service_encoder.fit_transform('InternetService')  # TODO: Fill this
# telecom_customer_data['Contract'] = contract_encoder.fit_transform('Contract')  # TODO: Fill this

telecom_customer_data['Churn'] = churn_encoder.fit_transform(telecom_customer_data['Churn'])
telecom_customer_data['InternetService'] = internet_service_encoder.fit_transform(telecom_customer_data['InternetService'])
telecom_customer_data['Contract'] = contract_encoder.fit_transform(telecom_customer_data['Contract'])


# 6. Save the encoders for use in the app
dump(churn_encoder, './models/churn_encoder.joblib')
dump(internet_service_encoder, './models/internet_service_encoder.joblib')
dump(contract_encoder, './models/contract_encoder.joblib')

# Save unique labels for 'InternetService' and 'Contract' for the app UI
labels_info = {
    'InternetService': list(internet_service_encoder.classes_),
    'Contract': list(contract_encoder.classes_)
}
labels_filepath = './models/feature_labels.json'
with open(labels_filepath, 'w') as f:
    json.dump(labels_info, f)
print(f"Feature labels saved at: {labels_filepath}")

# 7. Select features and target
# These are the columns the model will use for prediction
selected_features = ['tenure', 'InternetService', 'Contract', 'MonthlyCharges', 'TotalCharges']
X = telecom_customer_data[selected_features]
y = telecom_customer_data['Churn']

# 8. Train the Random Forest model
# TODO: Create a RandomForestClassifier with 100 trees and random_state=101
model = RandomForestClassifier(n_estimators=100, random_state=101)  # TODO: Fill this
# TODO: Fit the model on X and y
model.fit(X, y)  # TODO: Fill this
print("Model training completed.")

# 9. Save the trained model to a file
dump(model, model_filepath)
print(f"Trained model saved at: {model_filepath}")

# ===============================
# End of Script
# ===============================
