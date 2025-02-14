import streamlit as st

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

with col1:
    st.image("diesease_prediction.jpeg", width=300)  # Set to 300px width for uniformity
with col2:
    st.markdown("**1️⃣ Disease Prediction with AI** - AI models can analyze symptoms and predict diseases early. 👉 [Learn more](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7179009/)")

col3, col4 = st.columns(2)

with col3:
    st.markdown("**2️⃣ Medicine Image Classification** - AI-powered recognition helps classify medicines. 👉 [Read more](https://medimageclassification.streamlit.app/)")
with col4:
    st.image("imgae_classification.jpg", width=300)  # Set to 300px width for uniformity

col5, col6 = st.columns(2)

with col5:
    st.image("outpatient.jpeg", width=300)  # Set to 300px width for uniformity
with col6:
    st.markdown("**3️⃣ Predicting Outpatient Attendance** - AI can forecast patient volume. 👉 [Explore AI in Healthcare](https://www.healthcareitnews.com/news/how-ai-can-improve-patient-flow-and-hospital-operations)")

col7, col8 = st.columns(2)

with col7:
    st.markdown("**4️⃣ Bed Occupancy Prediction** - AI predicts hospital bed demand. 👉 [See AI's impact](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0266612)")
with col8:
    st.image("bed_occupancy.jpeg", width=300)  # Set to 300px width for uniformity
