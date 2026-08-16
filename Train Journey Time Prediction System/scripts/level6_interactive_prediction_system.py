import sys

def predict_journey_duration(distance_km, num_stops, departure_hour=8.0):
    w_distance = 0.0105
    w_stops = 0.3500
    b_intercept = 0.5000
    
    pred_duration = b_intercept + (w_distance * distance_km) + (w_stops * num_stops)
    
    dep_h = int(departure_hour)
    dep_m = int((departure_hour - dep_h) * 60)
    
    arr_hour_total = (departure_hour + pred_duration) % 24.0
    arr_h = int(arr_hour_total)
    arr_m = int((arr_hour_total - arr_h) * 60)
    
    dep_str = f"{dep_h:02d}:{dep_m:02d}"
    arr_str = f"{arr_h:02d}:{arr_m:02d}"
    
    avg_speed = round(distance_km / pred_duration, 2) if pred_duration > 0 else 0.0
    
    return {
        "distance_km": distance_km,
        "num_stops": num_stops,
        "departure_time": dep_str,
        "predicted_duration_hours": round(pred_duration, 2),
        "estimated_arrival_time": arr_str,
        "average_speed_kmh": avg_speed
    }

def print_visual_gauge(duration_hours):
    max_scale = 24.0
    bar_length = 30
    filled = int((min(duration_hours, max_scale) / max_scale) * bar_length)
    bar = "=" * filled + "-" * (bar_length - filled)
    print(f"Journey Gauge: [{bar}] ({duration_hours:.2f} hrs)")

def run_interactive_system():
    print("=" * 70)
    print("      SYSSLAN IT SOLUTIONS - TRAIN JOURNEY PREDICTION SYSTEM      ")
    print("=" * 70)
    print("Welcome to the Interactive Machine Learning Duration Predictor!\n")
    
    if len(sys.argv) > 1:
        dist_input = float(sys.argv[1])
        stops_input = int(sys.argv[2])
        dep_input = float(sys.argv[3]) if len(sys.argv) > 3 else 8.0
    else:
        print("Demo Mode (Preset Journey Inputs):")
        dist_input = 850.0
        stops_input = 6
        dep_input = 9.5
        print(f" - Distance: {dist_input} km")
        print(f" - Number of Stops: {stops_input}")
        print(f" - Departure Time: {dep_input} (9:30 AM)")
        
    result = predict_journey_duration(dist_input, stops_input, dep_input)
    
    print("\n" + "=" * 70)
    print("                       PREDICTION RESULTS                         ")
    print("=" * 70)
    print(f" Input Distance:         {result['distance_km']} km")
    print(f" Input Intermediate Stops:{result['num_stops']} stops")
    print(f" Scheduled Departure:    {result['departure_time']}")
    print("-" * 70)
    print(f" PREDICTED DURATION:     {result['predicted_duration_hours']} Hours")
    print(f" ESTIMATED ARRIVAL TIME: {result['estimated_arrival_time']}")
    print(f" ESTIMATED AVERAGE SPEED:{result['average_speed_kmh']} km/h")
    print("-" * 70)
    print_visual_gauge(result['predicted_duration_hours'])
    print("=" * 70)

if __name__ == "__main__":
    run_interactive_system()
