import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import joblib

# Load data
df = pd.read_csv("house_price_regression_dataset.csv")

# Split
X = df.drop('House_Price', axis=1)
y = df['House_Price']

# Scale
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train
model = LinearRegression()
model.fit(X_scaled, y)

# Save model & scaler
joblib.dump(model, "model.pkl")
joblib.dump(scaler, "scaler.pkl")

print("Model and scaler saved successfully.")