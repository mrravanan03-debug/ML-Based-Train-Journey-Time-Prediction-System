import csv
import os

def parse_time_to_hours(time_str):
    if not time_str or time_str.strip() == "":
        return None
    parts = time_str.strip().split(":")
    hours = int(parts[0])
    minutes = int(parts[1])
    return hours + (minutes / 60.0)

def calculate_duration(dep_str, arr_str):
    dep_h = parse_time_to_hours(dep_str)
    arr_h = parse_time_to_hours(arr_str)
    if dep_h is None or arr_h is None:
        return None
    duration = arr_h - dep_h
    if duration < 0:
        duration += 24.0
    return round(duration, 2)

def run_level_2_cleaning(input_csv, output_csv):
    print("=" * 65)
    print("TASK 2.1 & 2.2 & 2.3 & 2.4: DATA CLEANING AND FEATURE CREATION")
    print("=" * 65)
    
    with open(input_csv, mode='r', newline='', encoding='utf-8') as f:
        reader = list(csv.reader(f))
        
    header = reader[0]
    data_rows = reader[1:]
    
    seen_records = set()
    cleaned_rows = []
    removed_duplicates = 0
    
    for row in data_rows:
        row_tuple = tuple(row)
        if row_tuple in seen_records:
            removed_duplicates += 1
            continue
        seen_records.add(row_tuple)
        cleaned_rows.append(row)
        
    print(f"Duplicates Removed: {removed_duplicates}")
    print(f"Rows Remaining: {len(cleaned_rows)}")
    
    dist_idx = header.index("distance_km")
    stops_idx = header.index("num_stops")
    dep_idx = header.index("departure_time")
    arr_idx = header.index("arrival_time")
    
    valid_durations = []
    processed_records = []
    
    for row in cleaned_rows:
        dep_str = row[dep_idx]
        arr_str = row[arr_idx]
        dur = calculate_duration(dep_str, arr_str)
        if dur is not None:
            valid_durations.append(dur)
            
    avg_duration = round(sum(valid_durations) / len(valid_durations), 2) if valid_durations else 8.0
    print(f"Average Journey Duration (for Imputation): {avg_duration} hours")
    
    new_header = header + ["departure_hour", "arrival_hour", "duration_hours"]
    
    for row in cleaned_rows:
        dep_str = row[dep_idx]
        arr_str = row[arr_idx]
        
        dep_h = parse_time_to_hours(dep_str)
        arr_h = parse_time_to_hours(arr_str)
        
        dur = calculate_duration(dep_str, arr_str)
        if dur is None:
            print(f"Imputing missing duration for Train {row[0]} with average: {avg_duration} hrs")
            dur = avg_duration
            if arr_h is None and dep_h is not None:
                arr_h = round((dep_h + dur) % 24.0, 2)
                
        new_row = row + [str(round(dep_h, 2)), str(round(arr_h, 2)), str(dur)]
        processed_records.append(new_row)
        
    with open(output_csv, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(new_header)
        writer.writerows(processed_records)
        
    print(f"\nCleaned dataset successfully saved to: {output_csv}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    in_csv = os.path.join(base_dir, "data", "train_dataset.csv")
    out_csv = os.path.join(base_dir, "data", "cleaned_train_dataset.csv")
    run_level_2_cleaning(in_csv, out_csv)
