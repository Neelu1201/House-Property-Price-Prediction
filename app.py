import streamlit as st
import joblib

model = joblib.load('house_price_model.pkl')
features = joblib.load('model_features.pkl')

st.title("🏠 House Price Prediction App")

inputs = []

for f in features:
    val = st.number_input(f, value=0.0)
    inputs.append(val)

if st.button("Predict"):
    result = model.predict([inputs])
    st.success(result[0])