import streamlit as st
import numpy as np
import pandas as pd
import joblib

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="wide"
)

# -------------------- LOAD DATA --------------------
@st.cache_data
def load_data():
    return pd.read_csv("house_price_regression_dataset.csv")

df = load_data()

# -------------------- LOAD MODEL --------------------
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

# -------------------- HEADER --------------------
st.title("🏠 House Price Prediction System")
st.markdown("### Predict property prices based on key housing features")
st.markdown("---")

# -------------------- SIDEBAR --------------------
st.sidebar.header("⚙️ Input Features")

square_footage = st.sidebar.slider("Square Footage", 500, 5000, 2000)
bedrooms = st.sidebar.selectbox("Bedrooms", [1, 2, 3, 4, 5])
bathrooms = st.sidebar.selectbox("Bathrooms", [1, 2, 3])
year_built = st.sidebar.slider("Year Built", 1950, 2022, 2000)
lot_size = st.sidebar.slider("Lot Size", 0.5, 5.0, 2.5)
garage_size = st.sidebar.selectbox("Garage Size", [0, 1, 2])
neighborhood_quality = st.sidebar.slider("Neighborhood Quality", 1, 10, 5)

# -------------------- INPUT WARNINGS --------------------
if square_footage < 800:
    st.warning("Low square footage may significantly reduce price.")

# -------------------- MAIN LAYOUT --------------------
col1, col2 = st.columns(2)

# ---------- LEFT COLUMN ----------
with col1:
    st.subheader("📊 Input Summary")

    input_df = pd.DataFrame({
        "Feature": [
            "Square Footage", "Bedrooms", "Bathrooms",
            "Year Built", "Lot Size", "Garage Size",
            "Neighborhood Quality"
        ],
        "Value": [
            square_footage, bedrooms, bathrooms,
            year_built, lot_size, garage_size,
            neighborhood_quality
        ]
    })

    st.table(input_df)

# ---------- RIGHT COLUMN ----------
with col2:
    st.subheader("📈 Prediction")

    if st.button("Predict Price"):
        input_data = np.array([[square_footage, bedrooms, bathrooms,
                                year_built, lot_size, garage_size,
                                neighborhood_quality]])

        input_scaled = scaler.transform(input_data)
        prediction = model.predict(input_scaled)[0]

        # -------------------- MAIN OUTPUT --------------------
        st.metric("Estimated Price", f"₹ {int(prediction):,}")

        # -------------------- CONFIDENCE RANGE --------------------
        error_margin = 10000
        st.write(f"Estimated Range: ₹ {int(prediction - error_margin):,} - ₹ {int(prediction + error_margin):,}")

        # -------------------- INTERPRETATION --------------------
        if prediction > 800000:
            st.info("This property is in the premium price range.")
        elif prediction > 400000:
            st.info("This property is in the mid-range category.")
        else:
            st.info("This property is in the budget range.")

        # -------------------- FEATURE IMPORTANCE --------------------
        st.markdown("---")
        st.subheader("📊 Feature Importance")

        feature_names = [
            "Square Footage", "Bedrooms", "Bathrooms",
            "Year Built", "Lot Size", "Garage Size",
            "Neighborhood Quality"
        ]

        importance = model.coef_

        importance_df = pd.DataFrame({
            "Feature": feature_names,
            "Importance": importance
        }).sort_values(by="Importance", ascending=False)

        st.bar_chart(importance_df.set_index("Feature"))

        # -------------------- TOP FEATURE EXPLANATION --------------------
        top_feature = importance_df.iloc[0]['Feature']
        st.success(f"Most influential feature: {top_feature}")

        # -------------------- DOWNLOAD REPORT --------------------
        report = pd.DataFrame({
            "Predicted Price": [int(prediction)]
        })

        st.download_button(
            "📥 Download Prediction",
            report.to_csv(index=False),
            "prediction.csv"
        )

# -------------------- DATASET INSIGHTS --------------------
st.markdown("---")
with st.expander("📊 Dataset Insights"):
    st.write("Average Price:", int(df['House_Price'].mean()))
    st.write("Max Price:", int(df['House_Price'].max()))
    st.write("Min Price:", int(df['House_Price'].min()))

# -------------------- FOOTER --------------------
st.markdown("---")
st.markdown("Built with Streamlit | Machine Learning Regression Model")