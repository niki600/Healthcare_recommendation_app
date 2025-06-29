# data_preprocessing.py

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def preprocess_data(file_path='healthcare_data.csv'):
    # Load dataset
    df = pd.read_csv(file_path)
    print("Dataset loaded successfully!")

    # Handle missing values
    print("\nMissing values in each column:")
    print(df.isnull().sum())
    df.fillna(df.mean(numeric_only=True), inplace=True)

    # Split into features and target
    X = df.drop('Class', axis=1)
    y = df['Class']

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    print("\nFeatures scaled successfully!")

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )

    print("\nTraining samples:", X_train.shape[0])
    print("Testing samples:", X_test.shape[0])
    print("Data preprocessing complete!")

    return X_train, X_test, y_train, y_test, scaler
