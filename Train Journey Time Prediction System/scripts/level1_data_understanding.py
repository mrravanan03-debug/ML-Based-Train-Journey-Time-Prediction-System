import csv
import os

def analyze_train_dataset(file_path):
    print("=" * 65)
    print("TASK 1.1: CHECK THE DATASET FOR TOTAL RECORDS AND COLUMNS")
    print("=" * 65)
    
    with open(file_path, mode='r', newline='', encoding='utf-8') as f:
        reader = list(csv.reader(f))
        
    header = reader[0]
    data_rows = reader[1:]
    
    total_records = len(data_rows)
    total_columns = len(header)
    
    print(f"Total Records (Rows): {total_records}")
    print(f"Total Columns: {total_columns}")
    print("\nColumns List:")
    for idx, col_name in enumerate(header, start=1):
        print(f"  {idx}. {col_name}")

    print("\n" + "=" * 65)
    print("TASK 1.2: TRAIN-WISE TABLE SHOWING STARTING AND ENDING STATIONS")
    print("=" * 65)
    
    train_id_idx = header.index("train_id")
    train_name_idx = header.index("train_name")
    start_idx = header.index("start_station")
    end_idx = header.index("end_station")
    
    print(f"{'Train ID':<10} | {'Train Name':<20} | {'Start Station':<15} | {'End Station':<15}")
    print("-" * 70)
    
    seen_routes = set()
    for row in data_rows:
        train_id = row[train_id_idx]
        train_name = row[train_name_idx]
        start_st = row[start_idx]
        end_st = row[end_idx]
        
        route_key = (train_id, train_name, start_st, end_st)
        if route_key not in seen_routes:
            seen_routes.add(route_key)
            print(f"{train_id:<10} | {train_name:<20} | {start_st:<15} | {end_st:<15}")

    print("\n" + "=" * 65)
    print("TASK 1.3: CALCULATE BASIC STATISTICS FOR DISTANCE AND NUMBER OF STOPS")
    print("=" * 65)
    
    dist_idx = header.index("distance_km")
    stops_idx = header.index("num_stops")
    
    distances = [float(row[dist_idx]) for row in data_rows if row[dist_idx]]
    stops = [int(row[stops_idx]) for row in data_rows if row[stops_idx]]
    
    def calculate_stats(name, numbers):
        total_count = len(numbers)
        mean_val = sum(numbers) / total_count if total_count > 0 else 0
        min_val = min(numbers) if total_count > 0 else 0
        max_val = max(numbers) if total_count > 0 else 0
        print(f"Statistics for {name}:")
        print(f"  Count: {total_count}")
        print(f"  Mean (Average): {mean_val:.2f}")
        print(f"  Min Value: {min_val}")
        print(f"  Max Value: {max_val}")

    calculate_stats("Distance (km)", distances)
    print()
    calculate_stats("Number of Stops", stops)

    print("\n" + "=" * 65)
    print("TASK 1.4: IDENTIFY MISSING, DUPLICATE, OR INCORRECT VALUES")
    print("=" * 65)
    
    missing_counts = {col: 0 for col in header}
    for row in data_rows:
        for idx, val in enumerate(row):
            if val.strip() == "":
                missing_counts[header[idx]] += 1
                
    print("Missing Values Count per Column:")
    for col, count in missing_counts.items():
        print(f"  - {col}: {count} missing value(s)")
        
    seen_rows = set()
    duplicate_count = 0
    duplicate_rows_list = []
    
    for idx, row in enumerate(data_rows, start=1):
        row_tuple = tuple(row)
        if row_tuple in seen_rows:
            duplicate_count += 1
            duplicate_rows_list.append((idx, row))
        else:
            seen_rows.add(row_tuple)
            
    print(f"\nTotal Duplicate Records Found: {duplicate_count}")
    if duplicate_rows_list:
        print("Duplicate Row Details:")
        for row_num, row_data in duplicate_rows_list:
            print(f"  Row {row_num}: {row_data}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dataset_path = os.path.join(base_dir, "data", "train_dataset.csv")
    analyze_train_dataset(dataset_path)
