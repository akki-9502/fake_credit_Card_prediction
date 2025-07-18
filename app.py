import streamlit as st
import pickle

# List of input features your model expects
features = [
    'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
    'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20',
    'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'scaled_amount'
]

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("💳 Fake Credit Card Transaction Detection")
st.subheader("Enter transaction details below:")

# Collect user input for all features
user_inputs = []
for feature in features:
    val = st.number_input(f"{feature}", format="%.5f")
    user_inputs.append(val)

# Predict on button click
if st.button("Detect"):
    prediction = model.predict([user_inputs])
    if prediction[0] == 1:
        st.error("⚠️ Fraudulent transaction detected!")
    else:
        st.success("✅ Legitimate transaction.")
