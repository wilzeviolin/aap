import streamlit as st

# Set the page layout to wide
st.set_page_config(layout="wide")

# Homepage content
st.title("🏥 AI in Healthcare: Optimizing Resources & Accessibility")

st.image("healthcare_banner.jpg", use_container_width=True)
st.write("""
As Singapore’s healthcare system evolves, **leveraging cutting-edge technologies** becomes crucial.  
With **increasing demand** for medical services and resources, AI offers new possibilities to optimize healthcare.

> **“How can we leverage AI to optimize healthcare resources and improve accessibility for Singaporeans?”**
""")

st.subheader("🔍 How AI is Transforming Healthcare in Singapore")

# Apply Gestalt Principle of Continuation by alternating image and text placement
col1, col2 = st.columns(2)

# First image and text: image on the left
with col1:
    st.image("diesease_prediction.jpeg", width=300)  # Ensure uniform size for all images
with col2:
    st.markdown("**1️⃣ Disease Prediction with AI** - AI models can analyze symptoms and predict diseases early. 👉 [Learn more](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7179009/)")
    st.write("""
    AI-based disease prediction models can assist in early diagnosis, helping healthcare professionals to take preventive measures.  
    These AI tools analyze symptoms and other data to predict potential diseases before they become severe, reducing the burden on healthcare resources.
    """)

st.markdown("<hr>", unsafe_allow_html=True)  # Adding a horizontal line for separation

col3, col4 = st.columns(2)

# Second image and text: image on the right (aligned to the far right)
with col3:
    st.markdown("**2️⃣ Medicine Image Classification** - AI-powered recognition helps classify medicines. 👉 [Read more](https://medimageclassification.streamlit.app/)")
    st.write("""
    AI models are capable of recognizing and classifying various medicines based on their visual appearance.  
    This technology helps in streamlining pharmacy operations, reducing errors, and improving drug management in healthcare systems.
    """)
with col4:
    st.markdown(
        """
        <div style="display: flex; justify-content: flex-end;">
            <img src="imgae_classification.jpg" width="300">
        </div>
        """, 
        unsafe_allow_html=True
    )

st.markdown("<hr>", unsafe_allow_html=True)  # Adding a horizontal line for separation

col5, col6 = st.columns(2)

# Third image and text: image on the left
with col5:
    st.image("outpatient.jpeg", width=300)  # Ensure uniform size for all images
with col6:
    st.markdown("**3️⃣ Predicting Outpatient Attendance** - AI can forecast patient volume. 👉 [Explore AI in Healthcare](https://www.healthcareitnews.com/news/how-ai-can-improve-patient-flow-and-hospital-operations)")
    st.write("""
    AI helps healthcare providers predict outpatient attendance, allowing them to better allocate resources, manage staff, and optimize patient flow.  
    This leads to improved patient experience and operational efficiency.
    """)

st.markdown("<hr>", unsafe_allow_html=True)  # Adding a horizontal line for separation

col7, col8 = st.columns(2)

# Fourth image and text: image on the right (aligned to the far right)
with col7:
    st.markdown("**4️⃣ Bed Occupancy Prediction** - AI predicts hospital bed demand. 👉 [See AI's impact](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0266612)")
    st.write("""
    By analyzing past data and trends, AI can predict the demand for hospital beds, enabling hospitals to plan and prepare for future occupancy.  
    This optimizes hospital resources and reduces the strain on emergency services.
    """)
with col8:
    st.markdown(
        """
        <div style="display: flex; justify-content: flex-end;">
            <img src="bed_occupancy.jpeg" width="300">
        </div>
        """, 
        unsafe_allow_html=True
    )
