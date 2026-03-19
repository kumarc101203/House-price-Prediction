# 🏠 House Price Prediction System

A Machine Learning-based web application that predicts house prices based on key property features such as size, location quality, and amenities.

---

## 🚀 Project Overview

The real estate industry requires accurate estimation of property prices based on various features.  
This project builds a **regression model** and provides an **interactive Streamlit web application** for real-time predictions.

---

## 🎯 Objective

- Perform data analysis and preprocessing  
- Build and evaluate regression models  
- Identify key factors affecting house prices  
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
4. Feature Scaling  
5. Model Training:
   - Linear Regression  
   - KNN Regression  
6. Model Evaluation:
   - MAE, MSE, RMSE, MAPE  
   - R² Score & Adjusted R²  
7. Model Selection: **Linear Regression performed best**

---

## 📌 Key Insights

- **Square Footage** dominates prediction (~0.99 correlation)  
- Other features have minimal impact  
- Dataset is highly linear → results in near-perfect model performance  

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
├── app.py
├── train_model.py
├── model.pkl
├── scaler.pkl
├── house_price_regression_dataset.csv
├── requirements.txt
└── README.md


---

## ⚙️ Installation & Setup

1. Clone the repository:
```bash
git clone https://github.com/kumarc101203/House-price-Prediction.git
cd House-price-Prediction

#Install dependencies:

pip install -r requirements.txt

#Run the app:

streamlit run app.py

---------------------------------------------------------
*⚠️ Limitations*

- Dataset is highly linear and likely synthetic

- Model performance is dominated by one feature

- Real-world datasets may require more complex models

*🔮 Future Improvements*

- Use real-world datasets

- Try advanced models (Random Forest, XGBoost)

- Deploy on cloud

- Add API support

*👤 Author*

Kumar


*⭐ If you found this useful, consider giving it a star!*