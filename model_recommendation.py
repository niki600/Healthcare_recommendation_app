import pandas as pd
import pickle

# Loading model and scaler
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

def generate_recommendation(new_data):
    # Convert to DataFrame
    new_df = pd.DataFrame([new_data])

    # Ensure same column order as training
    new_df = new_df.reindex(columns=scaler.feature_names_in_)

    # Scale the data
    new_scaled = scaler.transform(new_df)

    # Predict
    prediction = model.predict(new_scaled)[0]
    
     # 🔹 Flip output to match your report/PPT mapping
    prediction = 1 - prediction

    # Return result
    if prediction == 0:
        return "No immediate action needed. Maintain your current health routine."
    else:
        return "Please consult a doctor or take medical advice."
