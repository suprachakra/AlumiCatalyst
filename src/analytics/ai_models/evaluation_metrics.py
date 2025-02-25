"""
Evaluation Metrics Module
This module calculates evaluation metrics for the predictive model.
"""

import numpy as np
from sklearn.metrics import mean_squared_error, r2_score

def evaluate_model(y_true: np.array, y_pred: np.array) -> dict:
    """
    Evaluate predictions using RMSE and R2 score.
    :param y_true: Actual target values.
    :param y_pred: Predicted target values.
    :return: Dictionary containing RMSE and R2 for each target.
    """
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)
    return {"RMSE": rmse, "R2": r2}

if __name__ == "__main__":
    # Example evaluation using dummy data
    y_true = np.array([[50, 20], [60, 25], [55, 22]])
    y_pred = np.array([[48, 19], [61, 24], [54, 23]])
    metrics = evaluate_model(y_true, y_pred)
    print("Evaluation Metrics:", metrics)
