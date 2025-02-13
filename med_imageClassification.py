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

# Initialize session state for navigation
if "page" not in st.session_state:
    st.session_state.page = "Homepage"

# Custom CSS for navbar
st.markdown("""
    <style>
        .navbar {
            display: flex;
            justify-content: center;
            gap: 30px;
            background-color: #f5f5f5;
            padding: 10px;
            border-radius: 10px;
        }
        .navbar button {
            border: none;
            background: none;
            font-size: 18px;
            font-weight: bold;
            color: black;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            transition: background 0.3s ease;
        }
        .navbar button:hover {
            background-color: #ddd;
        }
        .active {
            background-color: #4CAF50 !important;
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

# Create navigation bar with buttons
st.markdown('<div class="navbar">', unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    if st.button("🏠 Home", key="home_button"):
        st.session_state.page = "Homepage"

with col2:
    if st.button("📸 Image Classifier", key="classifier_button"):
        st.session_state.page = "ImageClassifier"

st.markdown('</div>', unsafe_allow_html=True)

# Display content based on selected page
if st.session_state.page == "Homepage":
    st.title("🏥 AI in Healthcare: Optimizing Resources & Accessibility")
    
    st.image("healthcare_banner.jpg", use_container_width=True)
    st.write("""
    As Singapore’s healthcare system evolves, **leveraging cutting-edge technologies** becomes crucial.  
    With **increasing demand** for medical services and resources, AI offers new possibilities to optimize healthcare.
    
    > **“How can we leverage AI to optimize healthcare resources and improve accessibility for Singaporeans?”**
    """)

    st.subheader("🔍 How AI is Transforming Healthcare in Singapore")

    # AI Applications
    st.image("disease_prediction.jpeg", width=300)
    st.markdown("**1️⃣ Disease Prediction with AI** - AI models can analyze symptoms and predict diseases early.  
    👉 [Learn more](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7179009/)")

    st.image("image_classification.jpg", width=300)
    st.markdown("**2️⃣ Medicine Image Classification** - AI-powered recognition helps classify medicines.  
    👉 [Read more](https://www.frontiersin.org/articles/10.3389/fphar.2021.700569/full)")

    st.image("outpatient.jpeg", width=300)
    st.markdown("**3️⃣ Predicting Outpatient Attendance** - AI can forecast patient volume.  
    👉 [Explore AI in Healthcare](https://www.healthcareitnews.com/news/how-ai-can-improve-patient-flow-and-hospital-operations)")

    st.image("bed_occupancy.jpeg", width=300)
    st.markdown("**4️⃣ Bed Occupancy Prediction** - AI predicts hospital bed demand.  
    👉 [See AI's impact](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0266612)")

elif st.session_state.page == "ImageClassifier":
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
        image = np.array(image) / 255.0  
        image = np.expand_dims(image, axis=0)

        # Make prediction
        prediction = model.predict(image)
        predicted_class = np.argmax(prediction)
        confidence = np.max(prediction)  

        # Show results
        st.subheader("Image Classification Prediction Result")
        st.write(f"### **Actual Class (from filename):** {actual_class}")
        st.write(f"### **Predicted Class:** {class_labels[predicted_class]}")
        st.write(f"### **Confidence:** {confidence:.2f}")

        # Check if prediction is correct
        if actual_class.lower() == class_labels[predicted_class].lower():
            st.success("✅ Prediction is correct!")
        else:
            st.error("❌ Prediction is incorrect.")
