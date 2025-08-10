import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

# =========================
# 1. Load Model
# =========================
MODEL_PATH = "CNN_from_Scratch.h5"
model = load_model(MODEL_PATH)

# Class names must match your dataset's folder names
# You can extract from your ImageDataGenerator or hardcode them
classes = ['Species1', 'Species2', 'Species3']  # Replace with actual class names

# =========================
# 2. Streamlit UI
# =========================
st.set_page_config(page_title="Fish Species Classifier", page_icon="🐟")
st.title("🐟 Multiclass Fish Image Classification")
st.markdown("Upload an image of a fish and let the model predict its species.")

# Upload Image
uploaded_file = st.file_uploader("Choose a fish image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display uploaded image
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    st.write("")

    # =========================
    # 3. Preprocess Image
    # =========================
    img = image.load_img(uploaded_file, target_size=(224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    # =========================
    # 4. Make Prediction
    # =========================
    predictions = model.predict(img_array)
    predicted_class = classes[np.argmax(predictions)]
    confidence = np.max(predictions) * 100

    # =========================
    # 5. Show Results
    # =========================
    st.subheader(f"Predicted Species: {predicted_class}")
    st.write(f"Confidence: {confidence:.2f}%")

    # Confidence per class
    st.write("### Model Confidence for All Classes:")
    for cls, prob in zip(classes, predictions[0]):
        st.write(f"{cls}: {prob*100:.2f}%")
