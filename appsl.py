import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load the saved model
model = tf.keras.models.load_model("finetune_mobilenetv2_new.h5")

# Define class labels
class_labels = {
    0: 'Alaxan',
    1: 'Bactidol',
    2: 'Bioflu',
    3: 'Biogesic',
    4: 'DayZinc',
    5: 'Decolgen',
    6: 'Fish Oil',
    7: 'Kremil S',
    8: 'Medicol',
    9: 'Neozep'
}

# Sidebar navigation (without affecting the main classification model)
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Homepage", "Model 1", "Model 2", "Model 3"])

# Main Content (Image Classifier stays on the main screen)
st.title("Image Classifier")
st.write("Upload an image to classify.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", width=500)  # Smaller image display

    # Preprocess image
    image = image.resize((224, 224))
    image = np.array(image) / 255.0  # Normalize
    image = np.expand_dims(image, axis=0)

    # Make prediction
    prediction = model.predict(image)
    predicted_class = np.argmax(prediction)
    confidence = np.max(prediction)

    # Display results
    st.subheader("Prediction Result")
    st.write(f"**Class:** {class_labels[predicted_class]}")
    st.write(f"**Confidence:** {confidence:.2f}")

# Sidebar pages (won't affect the main classification model)
if page == "Homepage":
    st.sidebar.write("Welcome to the Image Classifier!")

elif page == "Model 1":
    st.sidebar.write("Model 1 description goes here.")

elif page == "Model 2":
    st.sidebar.write("Model 2 description goes here.")

elif page == "Model 3":
    st.sidebar.write("Model 3 description goes here.")
