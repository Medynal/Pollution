# 🌍 Air Quality Analytics & AQI Prediction Platform

An end-to-end data analytics and machine learning application that explores, visualizes, and predicts Air Quality Index (AQI) levels across major cities in India.

Built with **Streamlit**, this project demonstrates practical skills in:

- Data cleaning & preprocessing  
- Exploratory Data Analysis (EDA)  
- Feature engineering  
- Regression & classification modelling  
- Model deployment  
**Link to application**: https://predictaqiandaqibucket.streamlit.app/
---

## 📌 Project Overview

Air pollution is a critical environmental and public health issue. This project analyzes historical air quality data (2015–2020) across multiple Indian cities and provides predictive insights using trained machine learning models.

The application allows users to:

- View and filter pollution data by city  
- Explore pollutant trends over time  
- Compare pollution levels across cities  
- Predict AQI values based on pollutant inputs  
- Classify AQI into health-based categories  

---

## 🧪 Dataset Information

The dataset contains air quality observations from multiple Indian cities between 2015 and 2020.

### Key Pollutants Included:

- **Particulate Matter:** PM2.5, PM10  
- **Nitrogen Compounds:** NO, NO₂, NOx  
- **Other Gases:** NH₃, CO, SO₂, O₃  
- **Volatile Organic Compounds (VOCs):** Benzene, Toluene, Xylene  

### Engineered Features

- Year  
- Month  
- Day  
- AQI  
- AQI Bucket (Category)  

---

## 🖥️ Application Features

### 1️⃣ Data Overview
- Dataset summary (records & features)  
- City-based filtering  
- Display of sample records  

### 2️⃣ Exploratory Data Analysis (EDA)

Interactive visualizations include:

- Pollutant trend over time (Line chart)  
- Average pollutant levels by city  
- Top 5 most polluted cities by selected pollutant  
- Correlation heatmap of pollutants  

### 3️⃣ Modelling & Prediction

Users can input:

- City  
- Date  
- Pollutant concentration values  

The system predicts:

- ✅ AQI (Regression Model)  
- 🏷️ AQI Category (Classification Model)  

---

## 🤖 Machine Learning Models

- `aqi_regressor.pkl` – AQI prediction model  
- `aqib_classifier.pkl` – AQI bucket classifier  
- `bucket_encoder.pkl` – Label encoder for AQI categories  

Models were serialized using Joblib for deployment.

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- Pandas  
- NumPy  
- Plotly  
- Scikit-learn  
- Joblib  
- Pillow  


