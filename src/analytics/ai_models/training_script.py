"""
Training Script for Predictive Model
Trains a multi-output predictive model for forecasting scrap loss and carbon emissions.
Uses historical data and saves the trained model.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
import pickle
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data(file_path: str) -> pd.DataFrame:
    logging.info("Loading training data...")
    return pd.read_csv(file_path)

def train_model(data: pd.DataFrame):
    features = data[['feature1', 'feature2', 'feature3']]
    targets = data[['scrap', 'emission']]
    X_train, X_test, y_train, y_test = train_test_split(features, targets, test_size=0.2, random_state=42)
    model = GradientBoostingRegressor(random_state=42)
    model.fit(X_train, y_train)
    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)
    logging.info("Model training complete; saved as 'model.pkl'.")

if __name__ == "__main__":
    data = load_data("historical_data.csv")
    train_model(data)
