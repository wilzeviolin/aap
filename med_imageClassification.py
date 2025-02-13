import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load the model
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("finetune_mobilenetv2_new.h5")

model = load_model()

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

# Sidebar Navigation
st.sidebar.title("Navigation")

# Add "Image Classifier" as the default page
page = st.sidebar.radio(
    "Go to", 
    ["🏠 Home", "📸 Image Classifier", "🩺 Disease Prediction", "📅 Outpatient Prediction", "🛏️ Bed Occupancy Prediction"],
    index=1  # Default is "Image Classifier"
)

# Redirect function using JavaScript
def redirect(url):
    st.markdown(f'<meta http-equiv="refresh" content="0; url={url}">', unsafe_allow_html=True)

# Navigation Logic (Redirect Instantly)
if page == "🏠 Home":
    redirect("https://maintrying.streamlit.app/")

elif page == "📸 Image Classifier":
    redirect("https://medimageclassification.streamlit.app/")

elif page == "🩺 Disease Prediction":
    redirect("https://your-disease-prediction-link")

elif page == "📅 Outpatient Prediction":
    redirect("https://your-outpatient-prediction-link")

elif page == "🛏️ Bed Occupancy Prediction":
    redirect("https://your-bed-occupancy-link")
