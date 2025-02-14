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
    st.markdown("**1️⃣ Disease Prediction with AI** - AI models can analyThyroid conditions are usually not life-threatening if diagnosed and treated properly. However, severe, untreated thyroid disorders can lead to serious complications.

Hypothyroidism (underactive thyroid): If left untreated, it can cause myxedema, a rare but life-threatening condition that leads to extreme fatigue, slow heart rate, and even coma.
Hyperthyroidism (overactive thyroid): If untreated, it can lead to a thyroid storm, a dangerous condition with high fever, rapid heartbeat, and organ failure.
Early diagnosis and treatment (medication, lifestyle changes, or surgery if needed) can prevent these complications. If you have symptoms like extreme fatigue, weight changes, or heart issues, it's best to see a doctor.ze symptoms and predict diseases early. 👉 [Learn more](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7179009/)")

st.markdown("<hr>", unsafe_allow_html=True)  # Adding a horizontal line for separation

col3, col4 = st.columns(2)

# Second image and text: image on the right (aligned to the far right)
with col3:
    st.markdown("**2️⃣ Medicine Image Classification** - AI-powered reThyroid conditions are usually not life-threatening if diagnosed and treated properly. However, severe, untreated thyroid disorders can lead to serious complications.

Hypothyroidism (underactive thyroid): If left untreated, it can cause myxedema, a rare but life-threatening condition that leads to extreme fatigue, slow heart rate, and even coma.
Hyperthyroidism (overactive thyroid): If untreated, it can lead to a thyroid storm, a dangerous condition with high fever, rapid heartbeat, and organ failure.
Early diagnosis and treatment (medication, lifestyle changes, or surgery if needed) can prevent these complications. If you have symptoms like extreme fatigue, weight changes, or heart issues, it's best to see a doctor.cognition helps classify medicines. 👉 [Read more](https://medimageclassification.streamlit.app/)")
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
    st.markdown("**3️⃣ Predicting Outpatient Attendance** - AI can forecast patient volume asdfThyroid conditions are usually not life-threatening if diagnosed and treated properly. However, severe, untreated thyroid disorders can lead to serious complications.

Hypothyroidism (underactive thyroid): If left untreated, it can cause myxedema, a rare but life-threatening condition that leads to extreme fatigue, slow heart rate, and even coma.
Hyperthyroidism (overactive thyroid): If untreated, it can lead to a thyroid storm, a dangerous condition with high fever, rapid heartbeat, and organ failure.
Early diagnosis and treatment (medication, lifestyle changes, or surgery if needed) can prevent these complications. If you have symptoms like extreme fatigue, weight changes, or heart issues, it's best to see a doctor.. 👉 [Explore AI in Healthcare](https://www.healthcareitnews.com/news/how-ai-can-improve-patient-flow-and-hospital-operations)")

st.markdown("<hr>", unsafe_allow_html=True)  # Adding a horizontal line for separation

col7, col8 = st.columns(2)

# Fourth image and text: image on the right (aligned to the far right)
with col7:
    st.markdown("**4️⃣ Bed Occupancy Prediction** - AI predicts hospital beThyroid conditions are usually not life-threatening if diagnosed and treated properly. However, severe, untreated thyroid disorders can lead to serious complications.

Hypothyroidism (underactive thyroid): If left untreated, it can cause myxedema, a rare but life-threatening condition that leads to extreme fatigue, slow heart rate, and even coma.
Hyperthyroidism (overactive thyroid): If untreated, it can lead to a thyroid storm, a dangerous condition with high fever, rapid heartbeat, and organ failure.
Early diagnosis and treatment (medication, lifestyle changes, or surgery if needed) can prevent these complications. If you have symptoms like extreme fatigue, weight changes, or heart issues, it's best to see a doctor.d demand. 👉 [See AI's impact](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0266612)")
with col8:
    st.markdown(
        """
        <div style="display: flex; justify-content: flex-end;">
            <img src="bed_occupancy.jpeg" width="300">
        </div>
        """, 
        unsafe_allow_html=True
    )
