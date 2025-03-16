
import streamlit as st

st.write('Hello, *World!* :sunglasses:')

git add app.py
git commit -m "Trigger reindexing"
git push origin main


import streamlit as st
import pickle  # or use import joblib if saved with joblib
import numpy as np

# Load the trained model
with open("model.pkl", "rb") as file:  # Ensure the model file is named correctly
    model = pickle.load(file)

st.title("🎯 Student Depression Prediction")

st.write("Enter your details below to predict the likelihood of depression.")

# Define input fields for user data (Modify these based on your dataset)
age = st.number_input("Age", min_value=10, max_value=100, step=1)
sleep_hours = st.number_input("Sleep Hours", min_value=0.0, max_value=24.0, step=0.1)
stress_level = st.slider("Stress Level (1-10)", 1, 10, 5)

# Convert inputs to a NumPy array (Modify this based on your model’s feature input format)
input_features = np.array([[age, sleep_hours, stress_level]])

# Make a prediction when the user clicks the button
if st.button("Predict"):
    prediction = model.predict(input_features)
    
    if prediction[0] == 1:
        st.error("⚠️ High chance of depression. Consider seeking professional help.")
    else:
        st.success("✅ Low chance of depression. Keep maintaining a healthy lifestyle!")

