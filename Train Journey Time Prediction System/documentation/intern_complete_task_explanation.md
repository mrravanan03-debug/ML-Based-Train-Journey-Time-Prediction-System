# Sysslan IT Solutions - Machine Learning Internship Cohort
## Master Project Task Explanation & Guide for Interns
**Project Title:** Machine Learning-Based Train Journey Time Prediction System  
**Level:** Beginner to Advanced (Levels 1 through 6 Complete)  

---

## 1. Executive Project Overview
Welcome to the complete Sysslan IT Solutions Machine Learning Internship project!

In real-world data science, building a machine learning system requires following an end-to-end workflow:
1. **Understanding the raw data**
2. **Cleaning noise and creating mathematical features**
3. **Exploring data relationships with visual insights**
4. **Training predictive machine learning algorithms**
5. **Evaluating and comparing model options**
6. **Deploying an interactive user-facing prediction system**

This master guide explains how every level was designed and implemented for a beginner intern.

---

## 2. Comprehensive Level-by-Level Breakdown

### Level 1: Understanding the Data
* **Task 1.1 (Dataset Size & Columns):** Loaded dataset containing 12 initial rows and 8 columns (`train_id`, `train_name`, `start_station`, `end_station`, `departure_time`, `arrival_time`, `distance_km`, `num_stops`).
* **Task 1.2 (Route Mapping):** Extracted start and end stations for all trains (e.g., Delhi to Mumbai, Chennai to Bengaluru).
* **Task 1.3 (Summary Statistics):** Calculated average distance ($651.83\text{ km}$) and average number of stops ($6.75\text{ stops}$).
* **Task 1.4 (Data Audit):** Detected 1 duplicate row (Train T110 Jan Shatabdi) and 1 missing value in `arrival_time` (Train T111 Local Fast).

---

### Level 2: Data Cleaning and Feature Creation
* **Task 2.1 (Handling Missing & Duplicates):** Removed duplicate records (dropping duplicate T110) and imputed missing arrival times using dataset average journey duration ($9.51\text{ hours}$).
* **Task 2.2 (Datetime Conversion):** Converted time strings (e.g., `"06:00"`, `"22:00"`) into floating-point hours (`6.0`, `22.0`) for mathematical ML processing.
* **Task 2.3 (Target Variable Creation):** Calculated `duration_hours = arrival_hour - departure_hour` as the target variable ($y$).
* **Task 2.4 (Feature Matrix):** Exported cleaned data to `data/cleaned_train_dataset.csv`.

---

### Level 3: Feature Analysis with Visuals
* **Task 3.1 & 3.2 (Visual Relationships):** Generated distance vs. duration and stops vs. duration visual bar distributions.
* **Task 3.3 (Correlation Analysis):**
  * Correlation (Distance vs Duration): $+0.8790$ (Very Strong correlation!)
  * Correlation (Stops vs Duration): $+0.4028$ (Moderate positive correlation)
* **Task 3.4 (Pivot Summary):** Calculated average train speeds across routes, identifying high-speed express trains ($94.88\text{ km/h}$ for Vande Bharat) vs. slower regional fast trains ($21.03\text{ km/h}$).

---

### Level 4 & Level 5: Model Training, Evaluation & Comparison
* **Task 4.1 (Train/Test Split):** Partitioned dataset into 80% Training Set (8 samples) and 20% Testing Set (3 samples).
* **Task 4.2 & 5.1 (Simple Model):** Trained a Single Feature Linear Regression model using Distance ($x_1$) only:
  $$\text{Duration} = 0.01077 \times \text{Distance} + 1.96030$$
* **Task 5.2 (Improved Multi-Feature Model):** Trained a Multi-Feature Linear Regression model using Distance ($x_1$) and Number of Stops ($x_2$):
  $$\text{Duration} = 0.0105 \times \text{Distance} + 0.3500 \times \text{Stops} + 0.5000$$
* **Task 5.3 & 5.4 (Model Selection):** The multi-feature model accounts for intermediate station delays, making it more robust for realistic travel predictions.

---

### Level 6: Final Interactive Machine Learning System
* **Task 6.1 (Interactive Prediction System):** Built `scripts/level6_interactive_prediction_system.py`, allowing users to enter any journey parameters (distance, stops, departure time) to immediately obtain predicted journey duration, arrival time, and speed.

---

## 3. How Interns Can Run All Python Scripts

Navigate into `Sysslan_ML_Internship_Project/scripts/` to execute any level:

1. **Run Level 1 Data Understanding:**
   ```bash
   python scripts/level1_data_understanding.py
   ```
2. **Run Level 2 Data Cleaning:**
   ```bash
   python scripts/level2_data_cleaning.py
   ```
3. **Run Level 3 Feature Analysis:**
   ```bash
   python scripts/level3_feature_analysis.py
   ```
4. **Run Level 4 & 5 Model Training & Evaluation:**
   ```bash
   python scripts/level4_5_model_training_comparison.py
   ```
5. **Run Level 6 Interactive Prediction System:**
   ```bash
   python scripts/level6_interactive_prediction_system.py 1200 8 06.0
   ```

---

## 4. Raw CSV Datasets

*(Attached after the explanation as per request instructions)*

### Dataset 1: Initial Raw Dataset (`data/train_dataset.csv`)

```csv
train_id,train_name,start_station,end_station,departure_time,arrival_time,distance_km,num_stops
T101,Rajdhani Express,Delhi,Mumbai,06:00,22:00,1384,8
T102,Shatabdi Express,Chennai,Bengaluru,06:00,11:00,350,4
T103,Duronto Express,Kolkata,Delhi,17:00,11:00,1447,5
T104,Garib Rath,Mumbai,Ahmedabad,07:50,14:40,491,6
T105,Vande Bharat,Delhi,Varanasi,06:00,14:00,759,4
T106,Tejas Express,Lucknow,Delhi,06:10,12:25,511,3
T107,Express Special,Bengaluru,Hyderabad,20:00,06:00,570,10
T108,Superfast Express,Pune,Nagpur,18:30,07:15,720,12
T109,Intercity Express,Ahmedabad,Surat,06:40,10:10,230,5
T110,Jan Shatabdi,Goa,Mumbai,11:30,20:15,580,9
T110,Jan Shatabdi,Goa,Mumbai,11:30,20:15,580,9
T111,Local Fast,Delhi,Agra,07:00,,200,6
```

---

### Dataset 2: Cleaned Feature Dataset (`data/cleaned_train_dataset.csv`)

```csv
train_id,train_name,start_station,end_station,departure_time,arrival_time,distance_km,num_stops,departure_hour,arrival_hour,duration_hours
T101,Rajdhani Express,Delhi,Mumbai,06:00,22:00,1384,8,6.0,22.0,16.0
T102,Shatabdi Express,Chennai,Bengaluru,06:00,11:00,350,4,6.0,11.0,5.0
T103,Duronto Express,Kolkata,Delhi,17:00,11:00,1447,5,17.0,11.0,18.0
T104,Garib Rath,Mumbai,Ahmedabad,07:50,14:40,491,6,7.83,14.67,6.83
T105,Vande Bharat,Delhi,Varanasi,06:00,14:00,759,4,6.0,14.0,8.0
T106,Tejas Express,Lucknow,Delhi,06:10,12:25,511,3,6.17,12.42,6.25
T107,Express Special,Bengaluru,Hyderabad,20:00,06:00,570,10,20.0,6.0,10.0
T108,Superfast Express,Pune,Nagpur,18:30,07:15,720,12,18.5,7.25,12.75
T109,Intercity Express,Ahmedabad,Surat,06:40,10:10,230,5,6.67,10.17,3.5
T110,Jan Shatabdi,Goa,Mumbai,11:30,20:15,580,9,11.5,20.25,8.75
T111,Local Fast,Delhi,Agra,07:00,,200,6,7.0,16.51,9.51
```
