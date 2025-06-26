import streamlit as st
from model_recommendation import generate_recommendation
from health_data_insight import show_insights 

# Show accuracy in sidebar
try:
    with open("accuracy.txt", "r") as f:
        accuracy_info = f.read()
    st.sidebar.info(accuracy_info)
except:
    st.sidebar.warning("Model accuracy not available.")

st.title("Personalized Healthcare Recommendation System")
st.markdown("Fill the details below to get a health recommendation.")

# checkbox to show EDA insights i.e graphs
if st.checkbox("Show Health Data Insights"):
    show_insights()
    st.stop() 
# Inputs
age = st.number_input("Age", min_value=1, max_value=100, value=30)
bp = st.number_input("Blood Pressure", min_value=80, max_value=200, value=120)
cholesterol = st.number_input("Cholesterol", min_value=100, max_value=300, value=180)
sugar = st.selectbox("Blood Sugar", ["Normal", "High"])
heart_rate = st.number_input("Heart Rate", min_value=40, max_value=180, value=75)
ecg = st.selectbox("ECG Result", ["Normal", "Abnormal"])
exercise = st.selectbox("Exercise Induced Angina", ["No", "Yes"])

# Dummy values for training-matched columns
frequency = 2
monetary = 500
recency = 10
time = 12

# Create input dictionary
input_data = {
    "Age": age,
    "Blood_Pressure": bp,
    "Cholesterol": cholesterol,
    "Blood_Sugar": 1 if sugar == "High" else 0,
    "Heart_Rate": heart_rate,
    "ECG_Result": 1 if ecg == "Abnormal" else 0,
    "Exercise_Induced_Angina": 1 if exercise == "Yes" else 0,
    "Frequency": frequency,
    "Monetary": monetary,
    "Recency": recency,
    "Time": time
}

if st.button("Get Recommendation"):
    result = generate_recommendation(input_data)
    st.success(result)
