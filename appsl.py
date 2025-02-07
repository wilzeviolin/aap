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
# Sidebar navigation (without affecting the main classification model)
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Homepage", "Model 1", "Model 2", "Model 3"])

# Streamlit UI
st.title("Medicine Image Classifier")

# Dropdown for selecting actual class
actual_class = st.selectbox("Select the actual class:", list(class_labels.values()))

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
    st.write(f"### **Actual Class:** {actual_class}")
    st.write(f"### **Predicted Class:** {class_labels[predicted_class]}")
    st.write(f"### **Confidence:** {confidence:.2f}")

    # Check if prediction is correct
    if actual_class == class_labels[predicted_class]:
        st.success("✅ Prediction is correct!")
    else:
        st.error("❌ Prediction is incorrect.")

# Sidebar pages (won't affect the main classification model)
if page == "Homepage":
    st.sidebar.write("Welcome to the Image Classifier!")

elif page == "Model 1":
    st.sidebar.write("Model 1 description goes here.")

elif page == "Model 2":
    st.sidebar.write("Model 2 description goes here.")

elif page == "Model 3":
    st.sidebar.write("Model 3 description goes here."
