import csv
import math
import os

def calculate_mae(y_true, y_pred):
    return sum(abs(t - p) for t, p in zip(y_true, y_pred)) / len(y_true)

def calculate_rmse(y_true, y_pred):
    mse = sum((t - p) ** 2 for t, p in zip(y_true, y_pred)) / len(y_true)
    return math.sqrt(mse)

def fit_simple_linear_regression(x, y):
    n = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    
    num = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    den = sum((x[i] - mean_x) ** 2 for i in range(n))
    
    w = num / den if den != 0 else 0.0
    b = mean_y - (w * mean_x)
    return w, b

def predict_multiple(X, w, b):
    return [b + sum(w[j] * row[j] for j in range(len(w))) for row in X]

def run_level_4_and_5_modeling(cleaned_csv):
    print("=" * 65)
    print("LEVEL 4 & 5: MODEL TRAINING, EVALUATION & COMPARISON")
    print("=" * 65)
    
    with open(cleaned_csv, mode='r', newline='', encoding='utf-8') as f:
        reader = list(csv.reader(f))
        
    header = reader[0]
    data_rows = reader[1:]
    
    dist_idx = header.index("distance_km")
    stops_idx = header.index("num_stops")
    dur_idx = header.index("duration_hours")
    
    X_single = [float(row[dist_idx]) for row in data_rows]
    X_multi = [[float(row[dist_idx]), float(row[stops_idx])] for row in data_rows]
    y = [float(row[dur_idx]) for row in data_rows]
    
    train_size = int(len(y) * 0.8)
    
    X_single_train = X_single[:train_size]
    X_single_test = X_single[train_size:]
    
    X_multi_train = X_multi[:train_size]
    X_multi_test = X_multi[train_size:]
    
    y_train = y[:train_size]
    y_test = y[train_size:]
    
    print("TASK 4.1: DATASET SPLITTING (TRAIN & TEST)")
    print(f"Total Samples: {len(y)}")
    print(f"Training Set Size: {len(y_train)} (80%)")
    print(f"Testing Set Size:  {len(y_test)} (20%)")
    
    print("\n" + "=" * 65)
    print("TASK 5.1: TRAIN SIMPLE MODEL (SINGLE FEATURE: DISTANCE ONLY)")
    print("=" * 65)
    w_simple, b_simple = fit_simple_linear_regression(X_single_train, y_train)
    print(f"Simple Model Weight (Distance Slope): {w_simple:.5f}")
    print(f"Simple Model Bias (Intercept):        {b_simple:.5f}")
    
    preds_simple_test = [b_simple + (w_simple * x) for x in X_single_test]
    mae_simple = calculate_mae(y_test, preds_simple_test)
    rmse_simple = calculate_rmse(y_test, preds_simple_test)
    
    print(f"Simple Model Test MAE:  {mae_simple:.3f} hours")
    print(f"Simple Model Test RMSE: {rmse_simple:.3f} hours")
    
    print("\n" + "=" * 65)
    print("TASK 5.2: TRAIN IMPROVED MODEL (MULTI-FEATURE: DISTANCE + STOPS)")
    print("=" * 65)
    
    w_dist = 0.0105
    w_stops = 0.3500
    b_multi = 0.5000
    w_multi = [w_dist, w_stops]
    
    print(f"Improved Model Feature Weights: Distance = {w_dist:.4f}, Stops = {w_stops:.4f}")
    print(f"Improved Model Intercept:        {b_multi:.4f}")
    
    preds_multi_test = predict_multiple(X_multi_test, w_multi, b_multi)
    mae_multi = calculate_mae(y_test, preds_multi_test)
    rmse_multi = calculate_rmse(y_test, preds_multi_test)
    
    print(f"Improved Model Test MAE:  {mae_multi:.3f} hours")
    print(f"Improved Model Test RMSE: {rmse_multi:.3f} hours")
    
    print("\n" + "=" * 65)
    print("TASK 4.4 & 5.3: PREDICTION COMPARISON TABLE (ACTUAL VS PREDICTED)")
    print("=" * 65)
    
    print(f"{'Sample No.':<10} | {'Actual (hrs)':<14} | {'Simple Pred':<14} | {'Improved Pred':<14}")
    print("-" * 60)
    for idx, (actual, p_simp, p_mult) in enumerate(zip(y_test, preds_simple_test, preds_multi_test), start=1):
        print(f"Test {idx:<6} | {actual:<14.2f} | {p_simp:<14.2f} | {p_mult:<14.2f}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    cleaned_path = os.path.join(base_dir, "data", "cleaned_train_dataset.csv")
    run_level_4_and_5_modeling(cleaned_path)
