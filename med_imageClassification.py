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

# Custom CSS for consistent button sizes
st.markdown("""
    <style>
        .navbar {
            display: flex;
            justify-content: space-around;
            background-color: white;
            padding: 15px;
            border-radius: 10px;
        }
        .navbar a {
            text-decoration: none;
        }
        .navbar button {
            border: none;
            background: none;
            font-size: 18px;
            font-weight: bold;
            color: black;
            padding: 12px 24px;
            border-radius: 30px;
            cursor: pointer;
            transition: background 0.3s ease, transform 0.3s ease;
            min-width: 200px;
            display: inline-block;
            text-align: center;
        }
        .navbar button:hover {
            background-color: #388E3C;
            color: white;
            transform: scale(1.05);
        }
    </style>
""", unsafe_allow_html=True)

# Create a navigation bar
st.markdown('<div class="navbar">', unsafe_allow_html=True)
st.markdown(
    """
    <a href="https://maintrying.streamlit.app/" target="_blank">
        <button>🏠 Home</button>
    </a>
    <a href="https://your-disease-prediction-deployment-link.com" target="_blank">
        <button>🩺 Disease Prediction</button>
    </a>
    <a href="https://your-outpatient-prediction-deployment-link.com" target="_blank">
        <button>📅 Outpatient Prediction</button>
    </a>
    <a href="https://your-bed-occupancy-deployment-link.com" target="_blank">
        <button>🛏 Bed Occupancy Prediction</button>
    </a>
    """,
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)

# Default page content for Home Page
st.title("📸 Medicine Image Classifier")
st.write("Upload an image to classify.")

uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Extract actual class from filename
    actual_class = uploaded_file.name.split("_")[0]

    # Preprocess the image
    image = image.resize((224, 224))
    image = np.array(image) / 255.0  # Normalize
    image = np.expand_dims(image, axis=0)

    # Make prediction
    prediction = model.predict(image)
    predicted_class = np.argmax(prediction)
    confidence = np.max(prediction)  # Get confidence score

    # Show results
    st.subheader("🔍 Classification Result")
    st.write(f"### **Actual Class:** {actual_class}")
    st.write(f"### **Predicted Class:** {class_labels[predicted_class]}")
    st.write(f"### **Confidence:** {confidence:.2f}")
