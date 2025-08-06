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

# Checkbox to show EDA insights
if st.checkbox("Show Health Data Insights"):
    show_insights()
    st.stop()

# -------------------------------
# Text to Numeric Mapping
# -------------------------------
blood_sugar_mapping = {
    "Normal": 90,
    "High": 160
}

ecg_mapping = {
    "Normal": 0,
    "Abnormal": 1
}

angina_mapping = {
    "No": 0,
    "Yes": 1
}

# -------------------------------
# Default Values
# -------------------------------
age = 30
bp = 120
cholesterol = 180
blood_sugar_text = "Normal"
heart_rate = 75
ecg_text = "Normal"
angina_text = "No"

recency = 6
frequency = 12
monetary = 55
time = 4

# -------------------------------
# Two quick test buttons
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    if st.button("Test Healthy Case"):
        age = 28
        bp = 110
        cholesterol = 170
        blood_sugar_text = "Normal"
        heart_rate = 75
        ecg_text = "Normal"
        angina_text = "No"
        recency = 6
        frequency = 12
        monetary = 55
        time = 4

with col2:
    if st.button("Test Medical Case"):
        age = 65
        bp = 185
        cholesterol = 260
        blood_sugar_text = "High"
        heart_rate = 75
        ecg_text = "Abnormal"
        angina_text = "Yes"
        recency = 1
        frequency = 2
        monetary = 10
        time = 1

# -------------------------------
# User Inputs (also editable)
# -------------------------------
age = st.number_input("Age", min_value=1, max_value=100, value=age)
bp = st.number_input("Blood Pressure", min_value=80, max_value=200, value=bp)
cholesterol = st.number_input("Cholesterol", min_value=100, max_value=300, value=cholesterol)
sugar_text = st.selectbox("Blood Sugar", ["Normal", "High"], index=0 if blood_sugar_text == "Normal" else 1)
heart_rate = st.number_input("Heart Rate", min_value=40, max_value=180, value=heart_rate)
ecg_text = st.selectbox("ECG Result", ["Normal", "Abnormal"], index=0 if ecg_text == "Normal" else 1)
exercise_text = st.selectbox("Exercise Induced Angina", ["No", "Yes"], index=0 if angina_text == "No" else 1)

recency = st.number_input("Recency", min_value=0, max_value=30, value=recency)
frequency = st.number_input("Frequency", min_value=0, max_value=50, value=frequency)
monetary = st.number_input("Monetary", min_value=0, max_value=1000, value=monetary)
time = st.number_input("Time", min_value=0, max_value=50, value=time)

# -------------------------------
# Convert to Numeric
# -------------------------------
blood_sugar = blood_sugar_mapping[sugar_text]
ecg = ecg_mapping[ecg_text]
exercise = angina_mapping[exercise_text]

# -------------------------------
# Create Input Dictionary
# -------------------------------
input_data = {
    "Age": age,
    "BP": bp,
    "Cholesterol": cholesterol,
    "BloodSugar": blood_sugar,
    "ECG": ecg,
    "Angina": exercise,
    "Recency": recency,
    "Frequency": frequency,
    "Monetary": monetary,
    "Time": time
}

# -------------------------------
# Prediction Button
# -------------------------------
if st.button("Get Recommendation"):
    result = generate_recommendation(input_data)
    if "No immediate action" in result:
        st.success(result)
    else:
        st.error(result)
