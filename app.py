import os
import gdown
import streamlit as st
from tensorflow.keras.models import load_model

st.title("Bird vs Drone Classifier")

if not os.path.exists("final_model.keras"):
    st.write("Downloading model...")
    url = "https://drive.google.com/uc?id=1lRta1xmVufV2xFvm6lVNWH6UKpmbTceR"
    gdown.download(url, "final_model.keras", quiet=False)

model = load_model("final_model.keras", compile=False)

st.write("Model loaded successfully")