import streamlit as st
import os
import gdown
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

st.title("Bird vs Drone Classifier")

# Step 1: Download model
if not os.path.exists("best_model.h5"):
    st.write("Downloading model... please wait ⏳")
    
    url = "https://drive.google.com/uc?id=1mmDg2CZ2b4rlNdmFulpFRkHXCL9n_9mo"
    gdown.download(url, "best_model.h5", quiet=False)

# Step 2: Load model
st.write("Loading model...")
model = load_model("best_model.h5")

# Step 3: Upload UI (IMPORTANT)
uploaded_file = st.file_uploader("Upload an image", type=["jpg","png","jpeg"])

# Step 4: Prediction
if uploaded_file is not None:
    img = image.load_img(uploaded_file, target_size=(224,224))
    st.image(img, caption="Uploaded Image")

    img_array = image.img_to_array(img)/255.0
    img_array = np.expand_dims(img_array, axis=0)

    pred = model.predict(img_array)

    if pred[0][0] > 0.5:
        st.success("Drone Detected 🚁")
    else:
        st.success("Bird Detected 🐦")

else:
    st.info("Please upload an image to start prediction")




https://drive.google.com/uc?id=1mmDg2CZ2b4rlNdmFulpFRkHXCL9n_9mo