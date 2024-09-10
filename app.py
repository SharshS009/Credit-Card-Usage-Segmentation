import streamlit as st
import numpy as np
import pickle  


with open('model.pkl', 'rb') as file:
    dt = pickle.load(file)

# Define the predict function
def predict(features):
    return dt.predict(np.array(features).reshape(1, -1))

# Define feature names 
feature_names = [

    "BALANCE", "BALANCE_FREQUENCY", "PURCHASES", "ONEOFF_PURCHASES",
    "INSTALLMENTS_PURCHASES", "CASH_ADVANCE", "PURCHASES_FREQUENCY",
    "ONEOFF_PURCHASES_FREQUENCY", "PURCHASES_INSTALLMENTS_FREQUENCY",
    "CASH_ADVANCE_FREQUENCY", "CASH_ADVANCE_TRX", "PURCHASES_TRX",
    "CREDIT_LIMIT", "PAYMENTS", "MINIMUM_PAYMENTS", "PRC_FULL_PAYMENT", "TENURE"
]

# Streamlit app title
st.title('Credit Card Usage Segment Prediction')

# Create input fields for each feature
user_input = []
for feature in feature_names:
    value = st.number_input(f'{feature}', value=0.0)
    user_input.append(value)

# Create a button for making predictions
if st.button('Predict'):
    prediction = predict(user_input)
    st.success(f'Predicted Segment: {prediction[0]}')
