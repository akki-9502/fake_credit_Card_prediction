app.py
import streamlit as st
import pandas as pd
import pickle  # or joblib, depending on how your model was saved

# Load the trained model (update path as needed)
model = pickle.load(open('model.pkl', 'rb'))  # Make sure you save your model to this file

st.title("Fake Credit Card Detection")

# Input form
st.subheader("Enter transaction details:")
feature_1 = st.number_input("Feature 1")
feature_2 = st.number_input("Feature 2")
# Add as many inputs as your model requires...

if st.button("Detect"):
    input_data = [[feature_1, feature_2]]  # Add all features in the correct order
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error("⚠️ Fraudulent transaction detected!")
    else:
        st.success("✅ Legitimate transaction.")
