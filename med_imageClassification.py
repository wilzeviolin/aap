import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import os

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

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Homepage", "Image Classifier"])

# Homepage
if page == "Homepage":
    st.title("🏥 AI in Healthcare: Optimizing Resources & Accessibility")
    
    # Introduction Section
    st.image("healthcare_banner.jpg", use_column_width=True)
    st.write("""
    As Singapore’s healthcare system evolves, **leveraging cutting-edge technologies** becomes crucial to addressing emerging challenges. 
    With **increasing demand** for medical services and resources, traditional approaches may no longer suffice.
    
    However, **Artificial Intelligence (AI)** offers new possibilities to enhance efficiency in hospitals, optimize healthcare resources, 
    and improve accessibility. This leads us to our **problem statement**:
    
    > **“How can we leverage AI to optimize healthcare resources and improve accessibility for Singaporeans?”**
    """)

    # AI Applications Section
    st.subheader("🔍 How AI is Transforming Healthcare in Singapore")
    
    # 1. Disease Prediction
    st.image("diesease_prediction.jpeg", width=300)
    st.markdown("""
    **1️⃣ Disease Prediction with AI**  
    AI models can analyze symptoms and predict possible diseases early, improving diagnostic efficiency.  
    👉 [Learn more](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7179009/)
    """)

    # 2. Medicine Classification
    st.image("imgae_classification.jpg", width=300)
    st.markdown("""
    **2️⃣ Medicine Image Classification**  
    AI-powered image recognition can help classify medicines, reducing errors in prescriptions and enhancing pharmaceutical management.  
    👉 [Read about AI in Pharma](https://www.frontiersin.org/articles/10.3389/fphar.2021.700569/full)
    """)

    # 3. Outpatient Attendance Prediction
    st.image("outpatient.jpeg", width=300)
    st.markdown("""
    **3️⃣ Predicting Outpatient Attendance**  
    AI can forecast patient volume at clinics and hospitals, allowing better staffing and resource allocation.  
    👉 [Explore AI in Healthcare Operations](https://www.healthcareitnews.com/news/how-ai-can-improve-patient-flow-and-hospital-operations)
    """)

    # 4. Bed Occupancy Prediction
    st.image("bed_occupancy.jpeg", width=300)
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
    
    Navigate through the sidebar to explore different AI models in action! 💡
    """)
# Image Classifier
elif page == "Image Classifier":
    st.title("Medicine Image Classifier")
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
        st.subheader("Image Classification Prediction Result")
        st.write(f"### **Actual Class (from filename):** {actual_class}")
        st.write(f"### **Predicted Class:** {class_labels[predicted_class]}")
        st.write(f"### **Confidence:** {confidence:.2f}")

        # Check if prediction is correct
        if actual_class.lower() == class_labels[predicted_class].lower():
            st.success("✅ Prediction is correct!")
        else:
            st.error("❌ Prediction is incorrect.")
