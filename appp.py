
import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
import os

# Load the trained model
@st.cache_resource
def load_model():
    model_path = 'sun_moon_model.h5'
    # On Streamlit Cloud, the model will be in the same directory as app.py
    # For local testing, ensure sun_moon_model.h5 is in the same folder
    if not os.path.exists(model_path):
        st.error(f"Model file not found at {model_path}.")
        st.stop()
    model = tf.keras.models.load_model(model_path)
    return model

model = load_model()

# Define class names (must match training order)
CLASS_NAMES = ['moon', 'sun']
IMAGE_SIZE = (224, 224)

st.title("SUN vs. MOON Image Classifier")
st.write("Upload an image to classify it as SUN or MOON!")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write("")
    st.write("Classifying...")

    # Preprocess the image
    img_array = np.array(image.resize(IMAGE_SIZE)) / 255.0 # Resize and normalize
    img_array = np.expand_dims(img_array, axis=0) # Add batch dimension

    # Make prediction
    predictions = model.predict(img_array)
    predicted_class_index = np.argmax(predictions)
    predicted_class_name = CLASS_NAMES[predicted_class_index]
    confidence = predictions[0][predicted_class_index] * 100

    st.success(f"Prediction: {predicted_class_name}")
    st.write(f"Confidence: {confidence:.2f}%")

