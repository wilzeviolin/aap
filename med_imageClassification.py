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

# Sidebar Navigation (Set Default to Image Classifier)
st.sidebar.title("Navigation")

if "page" not in st.session_state:
    st.session_state.page = "📸 Image Classifier"  # Default page

page = st.sidebar.radio(
    "Go to", 
    ["🏠 Home", "📸 Image Classifier", "🩺 Disease Prediction", "📅 Outpatient Prediction", "🛏️ Bed Occupancy Prediction"],
    index=1  # Default to Image Classifier
)

st.session_state.page = page  # Update session state

# Home (Redirects to your main Streamlit app)
if st.session_state.page == "🏠 Home":
    st.markdown("[Go to Main Page](https://maintrying.streamlit.app/)")

# Image Classifier (Default page)
elif st.session_state.page == "📸 Image Classifier":
    st.title("📸 Medicine Image Classifier")
    st.write("Upload an image to classify.")

    uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert('RGB')
        st.image(image, caption="Uploaded Image", use_column_width=True)

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
        st.write(f"### **Predicted Class:** {class_labels[predicted_class]}")
        st.write(f"### **Confidence:** {confidence:.2f}")

# Other Pages
elif st.session_state.page == "🩺 Disease Prediction":
    st.title("🩺 Disease Prediction")
    st.write("[Go to Disease Prediction](https://your-disease-prediction-link)")

elif st.session_state.page == "📅 Outpatient Prediction":
    st.title("📅 Outpatient Prediction")
    st.write("[Go to Outpatient Prediction](https://your-outpatient-prediction-link)")

elif st.session_state.page == "🛏️ Bed Occupancy Prediction":
    st.title("🛏️ Bed Occupancy Prediction")
    st.write("[Go to Bed Occupancy Prediction](https://your-bed-occupancy-link)")
