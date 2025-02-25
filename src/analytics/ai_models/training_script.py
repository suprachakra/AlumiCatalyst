"""
Training Script for Predictive Model
This script trains a sample model (using scikit-learn) on historical sensor data
and saves the model for inference.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
import pickle

def load_data(file_path: str) -> pd.DataFrame:
    # Load historical data from a CSV file
    return pd.read_csv(file_path)

def train_model(data: pd.DataFrame):
    # Assume data has columns: 'feature1', 'feature2', 'feature3', 'scrap', 'emission'
    features = data[['feature1', 'feature2', 'feature3']]
    # Stack scrap and emission as multi-output target
    targets = data[['scrap', 'emission']]
    
    X_train, X_test, y_train, y_test = train_test_split(features, targets, test_size=0.2, random_state=42)
    
    # Use a multi-output regressor (here simplified as training two independent models)
    model = GradientBoostingRegressor(random_state=42)
    model.fit(X_train, y_train)
    
    # Save the trained model
    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)
    
    print("Model training complete. Model saved as 'model.pkl'.")

if __name__ == "__main__":
    data = load_data("historical_data.csv")
    train_model(data)
