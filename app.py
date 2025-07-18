import streamlit as st
import pickle

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Fake Credit Card Detection")
st.subheader("Enter transaction details")

v1 = st.number_input("V1")
v2 = st.number_input("V2")
amount = st.number_input("Amount")

input_data = [[v1, v2, amount]]  # Must match the model's training feature order

if st.button("Detect"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error("⚠️ Fraudulent transaction detected!")
    else:
        st.success("✅ Legitimate transaction.")
