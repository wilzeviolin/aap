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

# Initialize session state for page tracking
if "page" not in st.session_state:
    st.session_state.page = "Homepage"

# Sidebar Navigation
st.sidebar.title("🔍 Navigation")
page = st.sidebar.radio("Go to", ["Homepage", "Disease Prediction", "Outpatient Prediction", "Bed Occupancy Prediction", "Image Classifier"])

st.markdown("<h1 style='text-align: center;'>Medicine Image Classifier</h1>", unsafe_allow_html=True)

# Top navigation buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("🏠 Home"):
        st.session_state.page = "Homepage"

with col2:
    if st.button("📸 Image Classifier"):
        st.session_state.page = "Image Classifier"

st.markdown("---")  # Divider

# Update session state based on sidebar selection
st.session_state.page = page

# Homepage
if st.session_state.page == "Homepage":
    st.title("🏥 Welcome to the AI-Powered Healthcare System")
    st.write("Use the buttons above or the sidebar to navigate.")
    st.image("homepage_banner.jpg", use_column_width=True)

# Disease Prediction Page
elif st.session_state.page == "Disease Prediction":
    st.title("🩺 Disease Prediction")
    st.write("AI can analyze symptoms and predict potential diseases.")
    st.write("[Go to Disease Prediction Model](https://your-disease-prediction-link)")

# Outpatient Prediction Page
elif st.session_state.page == "Outpatient Prediction":
    st.title("📅 Outpatient Prediction")
    st.write("Predict outpatient attendance trends with AI.")
    st.write("[Go to Outpatient Prediction Model](https://your-outpatient-prediction-link)")

# Bed Occupancy Prediction Page
elif st.session_state.page == "Bed Occupancy Prediction":
    st.title("🛏️ Bed Occupancy Prediction")
    st.write("Forecast hospital bed occupancy to optimize resources.")
    st.write("[Go to Bed Occupancy Model](https://your-bed-occupancy-link)")

# Image Classifier Page
elif st.session_state.page == "Image Classifier":
    st.title("📸 Medicine Image Classifier")
    st.write("Upload an image to classify.")

    uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert('RGB')
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Extract actual class from filename (assuming format: 'ClassName_#.jpg')
        actual_class = uploaded_file.name.split("_")[0]  # Gets the first part before "_"

        # Preprocess the image
        image = image.resize((224, 224))
        image = np.array(image) / 255.0  # Normalize
        image = np.expand_dims(image, axis=0)

        # Make prediction
        prediction = model.predict(image)
        predicted_class = np.argmax(prediction)
        confidence = np.max(prediction)  # Get confidence score

        # Show results
        st.subheader("🔍 Image Classification Prediction Result")
        st.write(f"### **Actual Class:** {actual_class}")
        st.write(f"### **Predicted Class:** {class_labels[predicted_class]}")
        st.write(f"### **Confidence:** {confidence:.2f}")

        # Check if prediction is correct
        if actual_class.lower() == class_labels[predicted_class].lower():
            st.success("✅ Prediction is correct!")
        else:
            st.error("❌ Prediction is incorrect.")
