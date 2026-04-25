#  AutoInsights – Automated Analytics System

A fully automated data analytics pipeline that transforms raw data into actionable insights, forecasts future trends, and triggers intelligent alerts — all with minimal human intervention.

---

##  Project Overview

AutoInsights is designed to simulate a real-world analytics system used in businesses.  
It not only analyzes historical data but also predicts future performance and detects anomalies automatically.

---

##  Key Features

-  Automated Data Cleaning & Preprocessing  
-  KPI Generation (Sales, Category, Region)  
-  Time-based Sales Analysis  
-  Sales Forecasting using Machine Learning  
-  Intelligent Alert System (drop/spike detection)  
-  Email Notifications for alerts  
-  Scheduled Automation  
-  Interactive Dashboard (Streamlit)  

---

## Tech Stack

- Python  
- Pandas, NumPy  
- Scikit-learn  
- Matplotlib  
- Streamlit  
- Schedule  

---

##  How to Run

### 1. Clone Repository


git clone https://github.com/Prerna-0908/Auto-Insights-Analytics-System.git
cd Auto-Insights-Analytics-System

### 2. Install Dependencies
   
    
  pip install -r requirements.txt

    
### 3. Run Analytics Pipeline

  python main.py


### 4. Run Dashboard

  
  python -m streamlit run app.py

  
### 5. Run Automation
   
   python scheduler.py

----

## Project Structure
- data_cleaning.py      → Data preprocessing

- analysis.py           → KPI calculations

- alerts.py             → Alert system

- forecast.py           → ML predictions

- visualization.py      → Charts

- scheduler.py          → Automation

- app.py                → Streamlit dashboard

- main.py               → Pipeline entry point

## Future Enhancements
- Real-time data integration
- Advanced ML models (ARIMA, LSTM)
- Cloud deployment
- User authentication
