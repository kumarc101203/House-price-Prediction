# 🏠 House Price Prediction System

A Machine Learning-based web application that predicts house prices based on key property features such as size, location quality, and amenities.

---

## 🚀 Project Overview

The real estate industry requires accurate price estimation based on property characteristics.  
This project builds a **regression model** to predict house prices and provides an **interactive web interface** using Streamlit.

---

## 🎯 Objective

- Analyze housing data
- Perform data preprocessing and EDA
- Train regression models
- Evaluate performance
- Deploy an interactive prediction system

---

## 📊 Features

- 📈 House price prediction using ML model
- 📊 Feature importance visualization
- 📉 Prediction range (confidence estimation)
- 🧠 Explainable output (key influencing feature)
- ⚠️ Input-based warnings
- 📥 Download prediction results
- 📊 Dataset insights dashboard

---

## 🧠 Machine Learning Pipeline

1. Data Loading & Inspection  
2. Data Cleaning (No missing values / duplicates found)  
3. Exploratory Data Analysis (EDA)  
4. Feature Engineering & Scaling  
5. Model Training:
   - Linear Regression
   - KNN Regression  
6. Model Evaluation:
   - MAE, MSE, RMSE, MAPE
   - R² Score & Adjusted R²  
7. Model Selection (Linear Regression performed best)

---

## 📌 Key Insights

- **Square Footage** has the highest impact on price (~0.99 correlation)
- Other features show weak to moderate influence
- Linear Regression achieved near-perfect performance due to strong linearity in data

---

## 🖥️ Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Streamlit

---

## 📂 Project Structure
house-price-prediction/
│
├── app.py # Streamlit UI
├── train_model.py # Model training script
├── model.pkl # Saved ML model
├── scaler.pkl # Saved scaler
├── house_price_regression_dataset.csv
├── requirements.txt
└── README.md


---

## ⚙️ Installation & Setup

1. Clone the repository:
```bash
git https://github.com/kumarc101203/House-price-Prediction.git
cd house-price-prediction


---

## ⚙️ Installation & Setup

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/house-price-prediction-ml.git
cd house-price-prediction-ml

# install dependencies
pip install -r requirements.txt

# run the app
streamlit run app.py