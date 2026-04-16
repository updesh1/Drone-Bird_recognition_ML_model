import os
import gdown
import streamlit as st
from tensorflow.keras.models import load_model

st.title("Bird vs Drone Classifier")

# Download model (.keras)
if not os.path.exists("final_model.keras"):
    st.write("Downloading model...")
    url = "https://drive.google.com/uc?id=19PlCSMEXGb6yHiM6AtIvP76xS_WyCSc1"
    gdown.download(url, "final_model.keras", quiet=False)

# Load model
model = load_model("final_model.keras", compile=False)

st.write("Model loaded successfully")