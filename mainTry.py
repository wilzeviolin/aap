import streamlit as st

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
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🏠 Home", key="home_button"):
        st.session_state.page = "Homepage"

with col2:
    if st.button("🩺 Disease Prediction", key="disease_prediction_button"):
        st.session_state.page = "DiseasePrediction"

with col3:
    if st.button("📸 Image Classifier", key="image_classifier_button"):
        st.session_state.page = "ImageClassifier"

with col4:
    if st.button("📅 Outpatient Prediction", key="outpatient_prediction_button"):
        st.session_state.page = "OutpatientPrediction"

st.markdown('</div>', unsafe_allow_html=True)

# Display content based on selected page
if st.session_state.page == "Homepage":
    st.title("🏥 AI in Healthcare: Optimizing Resources & Accessibility")

    st.image("healthcare_banner.jpg", use_container_width=True)
    
    st.write("""
    As Singapore’s healthcare system develops and continues to evolve throughout the years, leveraging cutting-edge technologies becomes an important factor to address emerging challenges in Singapore.  
    As the demand for medical services and resources continues to rise due to epidemiological transition, traditional approaches may no longer be enough to resolve these issues.  
    However, Artificial Intelligence (AI) may be able to provide help for our healthcare sector by offering them the potential to enhance efficiency in hospitals, optimise healthcare resources, and improve accessibility.  
    Hence, these possibilities lead us to form our problem statement: “How can we leverage AI to optimise healthcare resources and improve accessibility for Singaporeans?”
    """)

    # Add images and more details about AI applications
    st.subheader("🔍 How AI is Transforming Healthcare in Singapore")

    st.image("disease_prediction.jpeg", width=300)
    st.markdown("**1️⃣ Disease Prediction with AI** - AI models can analyze symptoms and predict diseases early.  
    👉 [Learn more about disease prediction](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7179009/)")

    st.image("image_classification.jpg", width=300)
    st.markdown("**2️⃣ Medicine Image Classification** - AI-powered recognition helps classify medicines.  
    👉 [Learn more about image classification](https://www.frontiersin.org/articles/10.3389/fphar.2021.700569/full)")

    st.image("outpatient.jpeg", width=300)
    st.markdown("**3️⃣ Predicting Outpatient Attendance** - AI can forecast patient volume.  
    👉 [Learn more about outpatient prediction](https://www.healthcareitnews.com/news/how-ai-can-improve-patient-flow-and-hospital-operations)")

    st.image("bed_occupancy.jpeg", width=300)
    st.markdown("**4️⃣ Bed Occupancy Prediction** - AI predicts hospital bed demand.  
    👉 [See more about bed occupancy prediction](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0266612)")

elif st.session_state.page == "DiseasePrediction":
    st.title("🩺 Disease Prediction with AI")
    st.write("This page will be linked to your disease prediction model.")
    # Link to disease prediction app
    st.write("[Go to Disease Prediction Model](diseasepredapp.py)")

elif st.session_state.page == "ImageClassifier":
    st.title("📸 Medicine Image Classifier")
    st.write("This page will be linked to your medicine image classification model.")
    # Link to image classifier app
    st.write("[Go to Image Classification Model](med_imageClassification.py)")

elif st.session_state.page == "OutpatientPrediction":
    st.title("📅 Outpatient Prediction")
    st.write("This page will be linked to your outpatient prediction model.")
    # Link to outpatient prediction app
    st.write("[Go to Outpatient Prediction Model](outpatient_prediction_app.py)")
