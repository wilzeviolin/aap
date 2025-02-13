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
    ["📸 Image Classifier", "🏠 Homepage", "🩺 Disease Prediction", "📅 Outpatient Prediction", "🛏️ Bed Occupancy Prediction"],
    index=0  # Set default to first option (Image Classifier)
)

st.session_state.page = page  # Update session state

# Image Classifier (Default page)
if st.session_state.page == "📸 Image Classifier":
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

# Homepage
elif st.session_state.page == "🏠 Homepage":
    st.title("🏥 AI in Healthcare")
    st.image("healthcare_banner.jpg", use_column_width=True)
    st.write("""
    AI is revolutionizing healthcare by improving efficiency, optimizing resources, and enhancing accessibility.  
    Explore how AI can transform Singapore's healthcare system.
    """)
    
    # Display AI applications with images (2x2 layout)
    col1, col2 = st.columns(2)

    with col1:
        st.image("disease_prediction.jpg", width=300)
        st.markdown("**🩺 Disease Prediction** - AI predicts diseases from symptoms. 👉 [Learn more](https://your-disease-prediction-link)")

        st.image("outpatient.jpg", width=300)
        st.markdown("**📅 Outpatient Prediction** - AI forecasts patient attendance. 👉 [Explore](https://your-outpatient-prediction-link)")

    with col2:
        st.image("image_classification.jpg", width=300)
        st.markdown("**📸 Medicine Image Classifier** - AI identifies medicines. 👉 [Read more](https://your-medicine-image-link)")

        st.image("bed_occupancy.jpg", width=300)
        st.markdown("**🛏️ Bed Occupancy Prediction** - AI predicts hospital bed demand. 👉 [See impact](https://your-bed-occupancy-link)")

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
