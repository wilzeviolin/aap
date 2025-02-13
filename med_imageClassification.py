import streamlit as st

# Initialize session state for navigation
if "current_page" not in st.session_state:
    st.session_state.current_page = "Homepage"

# Function to navigate between pages
def navigate(page):
    st.session_state.current_page = page

# Custom CSS for styling the navbar
st.markdown("""
    <style>
        .navbar {
            display: flex;
            justify-content: center;
            background-color: #4CAF50;
            padding: 10px;
            border-radius: 8px;
        }
        .navbar button {
            background: none;
            border: none;
            color: white;
            font-size: 18px;
            padding: 10px 20px;
            cursor: pointer;
        }
        .navbar button:hover {
            background: rgba(255, 255, 255, 0.2);
            border-radius: 5px;
        }
        .selected {
            font-weight: bold;
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

# Navbar
st.markdown('<div class="navbar">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 1])

with col1:
    if st.button("🏠 Homepage", key="home_btn"):
        navigate("Homepage")

with col2:
    if st.button("📷 Image Classifier", key="classifier_btn"):
        navigate("Image Classifier")

st.markdown('</div>', unsafe_allow_html=True)

# Page Content
if st.session_state.current_page == "Homepage":
    st.title("🏥 AI in Healthcare: Optimizing Resources & Accessibility")

    # Introduction Section
    st.image("healthcare_banner.jpg", use_container_width=True)
    st.write("""
    As Singapore’s healthcare system evolves, **leveraging cutting-edge technologies** becomes crucial to addressing emerging challenges. 
    With **increasing demand** for medical services and resources, traditional approaches may no longer suffice.
    
    However, **Artificial Intelligence (AI)** offers new possibilities to enhance efficiency in hospitals, optimize healthcare resources, 
    and improve accessibility. This leads us to our **problem statement**:
    
    > **“How can we leverage AI to optimize healthcare resources and improve accessibility for Singaporeans?”**
    """)

    # AI Applications Section
    st.subheader("🔍 How AI is Transforming Healthcare in Singapore")

    col1, col2 = st.columns(2)
    with col1:
        st.image("diesease_prediction.jpeg", use_container_width=True)
        st.markdown("""
        **1️⃣ Disease Prediction with AI**  
        AI models can analyze symptoms and predict possible diseases early, improving diagnostic efficiency.  
        👉 [Learn more](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7179009/)
        """)

    with col2:
        st.image("imgae_classification.jpg", use_container_width=True)
        st.markdown("""
        **2️⃣ Medicine Image Classification**  
        AI-powered image recognition can help classify medicines, reducing errors in prescriptions and enhancing pharmaceutical management.  
        👉 [Read about AI in Pharma](https://www.frontiersin.org/articles/10.3389/fphar.2021.700569/full)
        """)

    col3, col4 = st.columns(2)
    with col3:
        st.image("outpatient.jpeg", use_container_width=True)
        st.markdown("""
        **3️⃣ Predicting Outpatient Attendance**  
        AI can forecast patient volume at clinics and hospitals, allowing better staffing and resource allocation.  
        👉 [Explore AI in Healthcare Operations](https://www.healthcareitnews.com/news/how-ai-can-improve-patient-flow-and-hospital-operations)
        """)

    with col4:
        st.image("bed_occupancy.jpeg", use_container_width=True)
        st.markdown("""
        **4️⃣ Bed Occupancy Prediction**  
        AI can predict hospital bed demand, helping optimize patient flow and reducing waiting times.  
        👉 [See AI's impact on bed management](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0266612)
        """)

    # Conclusion
    st.subheader("🚀 The Future of AI in Healthcare")
    st.write("""
    AI-driven healthcare solutions can lead to **more efficient hospitals, improved patient care, and better resource utilization**. 
    With continuous advancements, AI will play a critical role in shaping **Singapore’s future healthcare landscape**.
    
    Navigate through the menu above to explore different AI models in action! 💡
    """)

elif st.session_state.current_page == "Image Classifier":
    st.title("Medicine Image Classifier")
    st.write("Upload an image to classify.")

    uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        from PIL import Image
        import tensorflow as tf
        import numpy as np

        model = tf.keras.models.load_model("finetune_mobilenetv2_new.h5")

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

        image = Image.open(uploaded_file).convert('RGB')
        st.image(image, caption="Uploaded Image", use_container_width=True)

        actual_class = uploaded_file.name.split("_")[0]  # Extract class from filename

        image = image.resize((224, 224))
        image = np.array(image) / 255.0  # Normalize
        image = np.expand_dims(image, axis=0)

        prediction = model.predict(image)
        predicted_class = np.argmax(prediction)
        confidence = np.max(prediction)

        st.subheader("Image Classification Prediction Result")
        st.write(f"### **Actual Class (from filename):** {actual_class}")
        st.write(f"### **Predicted Class:** {class_labels[predicted_class]}")
        st.write(f"### **Confidence:** {confidence:.2f}")

        if actual_class.lower() == class_labels[predicted_class].lower():
            st.success("✅ Prediction is correct!")
        else:
            st.error("❌ Prediction is incorrect.")
