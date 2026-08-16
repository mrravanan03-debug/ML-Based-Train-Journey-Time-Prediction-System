import csv
import math
import os

def calculate_mean(values):
    return sum(values) / len(values) if values else 0.0

def calculate_correlation(x, y):
    n = len(x)
    if n == 0:
        return 0.0
    mean_x = calculate_mean(x)
    mean_y = calculate_mean(y)
    
    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    denominator_x = math.sqrt(sum((x[i] - mean_x) ** 2 for i in range(n)))
    denominator_y = math.sqrt(sum((y[i] - mean_y) ** 2 for i in range(n)))
    
    if denominator_x * denominator_y == 0:
        return 0.0
    return numerator / (denominator_x * denominator_y)

def draw_ascii_chart(title, x_vals, y_vals, x_label, y_label):
    print("\n" + "=" * 65)
    print(f"VISUALIZATION: {title}")
    print("=" * 65)
    max_y = max(y_vals)
    for x, y in zip(x_vals, y_vals):
        bar_len = int((y / max_y) * 40)
        bar = "*" * bar_len
        print(f"{x_label} {x:<6} | {bar} ({y:.1f} {y_label})")

def run_level_3_analysis(cleaned_csv):
    with open(cleaned_csv, mode='r', newline='', encoding='utf-8') as f:
        reader = list(csv.reader(f))
        
    header = reader[0]
    data_rows = reader[1:]
    
    dist_idx = header.index("distance_km")
    stops_idx = header.index("num_stops")
    dur_idx = header.index("duration_hours")
    train_id_idx = header.index("train_id")
    train_name_idx = header.index("train_name")
    
    distances = [float(row[dist_idx]) for row in data_rows]
    stops = [int(row[stops_idx]) for row in data_rows]
    durations = [float(row[dur_idx]) for row in data_rows]
    
    print("TASK 3.1: VISUALIZE HOW DISTANCE AFFECTS JOURNEY DURATION")
    draw_ascii_chart("DISTANCE VS JOURNEY DURATION", distances, durations, "Distance (km)", "hrs")
    
    print("\nTASK 3.2: VISUALIZE IMPACT OF NUMBER OF STOPS ON JOURNEY DURATION")
    draw_ascii_chart("NUMBER OF STOPS VS JOURNEY DURATION", stops, durations, "Stops", "hrs")
    
    print("\n" + "=" * 65)
    print("TASK 3.3: CORRELATION ANALYSIS BETWEEN FEATURES AND DURATION")
    print("=" * 65)
    
    corr_dist_dur = calculate_correlation(distances, durations)
    corr_stops_dur = calculate_correlation(stops, durations)
    corr_dist_stops = calculate_correlation(distances, stops)
    
    print(f"Correlation (Distance vs Duration): {corr_dist_dur:.4f}")
    print(f"Correlation (Stops vs Duration):    {corr_stops_dur:.4f}")
    print(f"Correlation (Distance vs Stops):   {corr_dist_stops:.4f}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    cleaned_path = os.path.join(base_dir, "data", "cleaned_train_dataset.csv")
    run_level_3_analysis(cleaned_path)
