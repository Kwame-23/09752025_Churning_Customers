# Import necessary libraries
import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from keras.models import load_model

# Load the pre-trained models and encoders
with open('scaled.pkl', 'rb') as file:
    sc = pickle.load(file)

with open('categorical_encoder.pkl', 'rb') as file:
    label_encode = pickle.load(file)

# Load the feature-selected model
loaded_model = load_model('newmodel.h5')
# Load the feature-selected model
loaded_model = load_model('newmodel.h5')
# Load encoder
encoder = LabelEncoder()
def preprocess_input(data):
    
    categorical_cols = data.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        data[col] = encoder.transform(data[col])

    # Scale the features
    X = sc.transform(data)
    return X


st.title("Churningzzzzzz")
st.subheader("Input the following features:")
st.text("Kwame Afriyie-Buabeng")
st.markdown("\n\n\n\n\n\n")
l, m ,r = st.columns(3)

with l:

    gender = st.radio("Gender", ["Male", "Female"])
    Partner = st.radio("Partner", ["Yes", "No"])
    Dependents = st.radio("Dependents", ["Yes", "No"])
    PhoneService = st.radio("PhoneService", ["Yes", "No"])
    MultipleLines = st.radio("MultipleLines", ["Yes", "No", "No phone service"])
    InternetService = st.radio("InternetService", ["DSL", "Fiber optic", "No"])
with m:    
    OnlineSecurity = st.radio("OnlineSecurity", ["Yes", "No"])
    OnlineBackup = st.radio("OnlineBackup", ["Yes", "No"])
    DeviceProtection = st.radio("DeviceProtection", ["Yes", "No"])
    TechSupport = st.radio("TechSupport", ["Yes", "No"])
    StreamingTV = st.radio("StreamingTV", ["Yes", "No"])
    StreamingMovies = st.radio("StreamingMovies", ["Yes", "No"])
with r:    
        Contract = st.radio("Contract", ["Month-to-month", "One year", "Two year"])
        PaperlessBilling = st.radio("PaperlessBilling", ["Yes", "No"])
        PaymentMethod = st.radio("PaymentMethod", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
        SeniorCitizen = st.radio("SeniorCitizen", ["Yes", "No"])
        tenure = st.number_input("Tenure", min_value=0.0, max_value=75.0)
        MonthlyCharges = st.number_input("MonthlyCharges($)", min_value=0.0)
        TotalCharges = st.number_input("TotalCharges($)", min_value=0.0)
    
st.markdown("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

if st.button("Predict Churn"):
    user_data = pd.DataFrame({
        'gender': [gender],
        'Partner': [Partner],
        'Dependents': [Dependents],
        'PhoneService': [PhoneService],
        'MultipleLines': [MultipleLines],
        'InternetService': [InternetService],
        'OnlineSecurity': [OnlineSecurity],
        'OnlineBackup': [OnlineBackup],
        'DeviceProtection': [DeviceProtection],
        'TechSupport': [TechSupport],
        'StreamingTV': [StreamingTV],
        'StreamingMovies': [StreamingMovies],
        'Contract': [Contract],
        'PaperlessBilling': [PaperlessBilling],
        'PaymentMethod': [PaymentMethod],
        'SeniorCitizen': [SeniorCitizen],
        'tenure': [tenure],
        'MonthlyCharges': [MonthlyCharges],
        'TotalCharges': [TotalCharges],
    })

    # Preprocess the user input
    processed_data = preprocess_input(user_data)

    # Make predictions
    prediction = loaded_model.predict(processed_data)

    # Determine churn likelihood and display result
    churn_likelihood = prediction[0]
    
    if churn_likelihood > 0.5:
        st.warning("Warning: The user is likely to churn!")
    else:
        st.success("Great news: The user is less likely to churn!")

   