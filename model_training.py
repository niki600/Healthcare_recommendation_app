import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# Load dataset
df = pd.read_csv('healthcare_data.csv')

# Features and label
X = df.drop('Class', axis=1)
y = df['Class']

# Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_scaled, y)

# ✅ Accuracy Calculation
y_pred = model.predict(X_scaled)
accuracy = accuracy_score(y, y_pred)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

# Save scaler
with open("scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

# ✅ Save accuracy to file
with open("accuracy.txt", "w") as f:
    f.write(f"Model Accuracy: {accuracy * 100:.2f}%")

print("✅ Model, scaler and accuracy.txt saved successfully.")
