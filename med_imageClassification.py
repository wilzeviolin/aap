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

# Custom CSS to style the navigation bar and buttons
st.markdown("""
    <style>
        .navbar {
            display: flex;
            justify-content: space-around; /* Slightly tighter spacing */
            background-color: white;
            padding: 15px 0;
            border-radius: 10px;
        }
        .navbar a {
            text-decoration: none;
            flex-grow: 1;
            text-align: center;
        }
        .navbar button {
            border: none;
            font-size: 16px;
            font-weight: bold;
            color: white;
            padding: 14px 28px;
            border-radius: 10px;
            cursor: pointer;
            transition: background 0.3s ease, transform 0.3s ease;
            background-color: #4CAF50;
            width: 100%;
            height: 50px;
        }
        .navbar button:hover {
            background-color: #388E3C;
            transform: scale(1.05);
        }
        /* Home button padding adjustment */
        .home-btn {
            padding: 14px 28px !important;
        }
    </style>
""", unsafe_allow_html=True)

# Create navigation bar using Streamlit columns
st.markdown('<div class="navbar">', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4, gap="small")  # Reduced gap

with col1:
    st.markdown('<a href="https://maintrying.streamlit.app/" target="_self">'
                '<button class="home-btn">🏠 Home</button></a>', unsafe_allow_html=True)

with col2:
    st.markdown('<a href="https://your-disease-prediction-deployment-link.com" target="_self">'
                '<button>🩺 Disease Prediction</button></a>', unsafe_allow_html=True)

with col3:
    st.markdown('<a href="https://your-outpatient-prediction-deployment-link.com" target="_self">'
                '<button>📅 Outpatient Prediction</button></a>', unsafe_allow_html=True)

with col4:
    st.markdown('<a href="https://your-bed-occupancy-deployment-link.com" target="_self">'
                '<button>🛏 Bed Occupancy Prediction</button></a>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Default page content 
