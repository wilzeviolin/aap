import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Initialize session state for navigation
if "page" not in st.session_state:
    st.session_state.page = "Homepage"

# Custom CSS for a cleaner navbar design
st.markdown("""
    <style>
        .navbar {
            display: flex;
            justify-content: center;
            gap: 20px;
            background-color: #4CAF50;
            padding: 15px 0;
            border-radius: 50px;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
        }
        .navbar button {
            border: none;
            background: none;
            font-size: 18px;
            font-weight: bold;
            color: white;
            padding: 12px 24px;
            border-radius: 50px;
            cursor: pointer;
            transition: background 0.3s ease, transform 0.3s ease;
        }
        .navbar button:hover {
            background-color: #388E3C;
            transform: scale(1.05);
        }
        .navbar .active {
            background-color: #388E3C !important;
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

# Create navigation bar with buttons
st.markdown('<div class="navbar">', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🏠 Home", key="home_button"):
        st.session_state.page = "Homepage"
with col2:
    if st.button("📸 Image Classifier", key="classifier_button"):
        st.session_state.page = "ImageClassifier"
with col3:
    if st.button("🩺 Disease Prediction", key="disease_prediction_button"):
        st.session_state.page = "DiseasePrediction"
with col4:
    if st.button("📅 Outpatient Prediction", key="outpatient_prediction_button"):
        st.session_state.page = "OutpatientPrediction"

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
    st.image("diesease_prediction.jpeg", width=300)
    st.markdown("**1️⃣ Disease Prediction with AI** - AI models can analyze symptoms and predict diseases early. 👉 [Learn more](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7179009/)")

    st.image("imgae_classification.jpg", width=300)
    st.markdown("**2️⃣ Medicine Image Classification** - AI-powered recognition helps classify medicines. 👉 [Read more](https://medimageclassification.streamlit.app/)")

    st.image("outpatient.jpeg", width=300)
    st.markdown("**3️⃣ Predicting Outpatient Attendance** - AI can forecast patient volume. 👉 [Explore AI in Healthcare](https://www.healthcareitnews.com/news/how-ai-can-improve-patient-flow-and-hospital-operations)")

    st.image("bed_occupancy.jpeg", width=300)
    st.markdown("**4️⃣ Bed Occupancy Prediction** - AI predicts hospital bed demand.  👉 [See AI's impact](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0266612)")

elif st.session_state.page == "DiseasePrediction":
    st.title("🩺 Disease Prediction with AI")
    st.write("This page will be linked to your disease prediction model.")
    # Link to disease prediction app
    st.write("[Go to Disease Prediction Model](diseasepredapp.py)")

elif st.session_state.page == "ImageClassifier":
    st.title("📸 Medicine Image Classifier")
    st.write("This page will be linked to your medicine image classification model.")
    # Link to image classifier app
    st.write("[Go to Image Classification Model](https://medimageclassification.streamlit.app/)")

elif st.session_state.page == "OutpatientPrediction":
    st.title("📅 Outpatient Prediction")
    st.write("This page will be linked to your outpatient prediction model.")
    # Link to outpatient prediction app
    st.write("[Go to Outpatient Prediction Model](outpatient_prediction_app.py)")
