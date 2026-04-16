import os
import gdown
import streamlit as st
from tensorflow.keras.models import load_model

st.title("Bird vs Drone Classifier")

# Download model (.h5)
if not os.path.exists("final_model.h5"):
    st.write("Downloading model...")
    url = "https://drive.google.com/uc?id=18-_QBibUvx3WIYZgMi_Sl4u0ar7gHSgI"
    gdown.download(url, "final_model.h5", quiet=False)

# Load model
model = load_model("final_model.h5", compile=False)

st.write("Model loaded successfully")