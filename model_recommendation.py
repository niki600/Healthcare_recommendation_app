import pandas as pd
import pickle

# Load model and scaler
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

def generate_recommendation(new_data):
    new_df = pd.DataFrame([new_data])
    new_scaled = scaler.transform(new_df.reindex(columns=scaler.feature_names_in_))
    prediction = model.predict(new_scaled)[0]

    if prediction == 0:
        return "✅ No immediate action needed. Maintain your current health routine."
    else:
        return "🚨 Please consult a doctor or take medical advice."

