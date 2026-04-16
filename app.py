import os
import gdown
import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

# Page setup
st.set_page_config(page_title="Bird vs Drone", layout="centered")

st.title("Bird vs Drone Classifier")

st.write(
    "Upload an image and the model will recognize out whether it's a bird or a drone."
)

# Download model if not already present
model_path = "final_model.h5"

if not os.path.exists(model_path):
    st.info("Downloading model... (this happens only once)")
    url = "https://drive.google.com/uc?id=18-_QBibUvx3WIYZgMi_Sl4u0ar7gHSgI"
    gdown.download(url, model_path, quiet=False)

# Load model
model = load_model(model_path, compile=False)

st.success("Model is ready!")

# Upload section
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Show image
    img = image.load_img(uploaded_file, target_size=(224, 224))
    st.image(img, caption="Your uploaded image", use_container_width=True)

    # Prepare image
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    st.write("Analyzing...")
    prediction = model.predict(img_array)

    score = float(prediction[0][0])

    drone_prob = score
    bird_prob = 1 - score

    st.write("---")

    if score > 0.5:
        st.write("Result: Drone")
    else:
        st.write("Result: Bird")

    st.write(f"Drone Probability: {drone_prob:.4f}")
    st.write(f"Bird Probability: {bird_prob:.4f}")

    st.progress(int(max(drone_prob, bird_prob) * 100))

# Small footer
st.write("---")
st.caption("Simple image classifier built with TensorFlow and Streamlit")