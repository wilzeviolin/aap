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

# Get page from query parameters (default to Homepage)
query_params = st.query_params
page = query_params.get("page", "Homepage")

# Custom CSS for a modern navbar
st.markdown("""
    <style>
        .navbar {
            display: flex;
            justify-content: center;
            gap: 30px;
            background-color: #f5f5f5;
            padding: 12px;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        .navbar a {
            text-decoration: none;
            font-size: 18px;
            font-weight: bold;
            color: black;
            padding: 10px 20px;
            border-radius: 5px;
            transition: background 0.3s ease;
        }
        .navbar a:hover {
            background-color: #ddd;
        }
        .active {
            background-color: #4CAF50;
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

# Navbar
st.markdown(f"""
    <div class="navbar">
        <a href="?page=Homepage" class="{'active' if page == 'Homepage' else ''}">🏠 Home</a>
        <a href="?page=ImageClassifier" class="{'active' if page == 'ImageClassifier' else ''}">📸 Image Classifier</a>
    </div>
""", unsafe_allow_html=True)

# Homepage Content
if page == "Homepage":
    st.title("🏥 AI in Healthcare: Optimizing Resources & Accessibility")
    
    # Introduction
    st.image("healthcare_banner.jpg", use_container_width=True)
    st.write("""
    As Singapore’s healthcare system evolves, **leveraging AI** becomes crucial for optimizing resources.
    
    > **“How can we use AI to enhance healthcare efficiency and accessibility in Singapore?”**
    """)

    # AI Applications
    st.subheader("🔍 How AI is Transforming Healthcare in Singapore")

    # 1. Disease Prediction
    st.image("diesease_prediction.jpeg", width=300)
    st.markdown("""
    **1️⃣ Disease Prediction with AI**  
    AI helps predict diseases early, improving diagnostics.  
    👉 [Learn more](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7179009/)
    """)

    # 2. Medicine Classification
    st.image("imgae_classification.jpg", width=300)
    st.markdown("""
    **2️⃣ Medicine Image Classification**  
    AI helps classify medicines, reducing errors in prescriptions.  
    👉 [Read more](https://www.frontiersin.org/articles/10.3389/fphar.2021.700569/full)
    """)

    # 3. Outpatient Attendance Prediction
    st.image("outpatient.jpeg", width=300)
    st.markdown("""
    **3️⃣ Predicting Outpatient Attendance**  
    AI forecasts patient volume, allowing better hospital planning.  
    👉 [Explore AI in hospitals](https://www.healthcareitnews.com/news/how-ai-can-improve-patient-flow-and-hospital-operations)
    """)

    # 4. Bed Occupancy Prediction
    st.image("bed_occupancy.jpeg", width=300)
    st.markdown("""
    **4️⃣ Bed Occupancy Prediction**  
    AI predicts hospital bed demand, reducing waiting times.  
    👉 [See AI’s impact on bed management](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0266612)
    """)

    # Conclusion
    st.subheader("🚀 The Future of AI in Healthcare")
    st.write("""
    AI will play a key role in **improving healthcare operations and patient outcomes**.
    Navigate using the **menu above** to explore different AI models in action! 💡
    """)

# Image Classifier Page
elif page == "ImageClassifier":
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

        # Display Results
        st.subheader("Image Classification Prediction Result")
        st.write(f"### **Actual Class (from filename):** {actual_class}")
        st.write(f"### **Predicted Class:** {class_labels[predicted_class]}")
        st.write(f"### **Confidence:** {confidence:.2f}")

        # Check if prediction is correct
        if actual_class.lower() == class_labels[predicted_class].lower():
            st.success("✅ Prediction is correct!")
        else:
            st.error("❌ Prediction is incorrect.")
