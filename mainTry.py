import streamlit as st

# Set the page layout to wide
st.set_page_config(layout="wide")

# Custom CSS for full-width text and proper alignment
st.markdown("""
    <style>
        .full-width-text {
            text-align: justify;
            font-size: 18px;
            line-height: 1.6;
        }
        .image-container {
            display: flex;
            justify-content: flex-end;
        }
    </style>
""", unsafe_allow_html=True)

# Full-width introductory section
st.title("🏥 AI in Healthcare: Optimizing Resources & Accessibility")

st.image("healthcare_banner.jpg", use_container_width=True)

st.markdown("""
    <div class="full-width-text">
        As Singapore’s healthcare system evolves, <b>leveraging cutting-edge technologies</b> becomes crucial.  
        With the nation's <b>aging population and increasing demand</b> for medical services, AI provides an opportunity to optimize healthcare delivery.  

        **AI-driven solutions** are helping in disease prediction, outpatient management, and resource allocation, ensuring that patients receive the care they need efficiently.  
        By integrating AI, healthcare providers can reduce bottlenecks, improve diagnostics, and enhance the patient experience.  

        <b>How can AI help optimize healthcare resources and improve accessibility for Singaporeans?</b>
    </div>
""", unsafe_allow_html=True)

st.subheader("🔍 How AI is Transforming Healthcare in Singapore")

# AI Applications with Proper Image Alignment

## Disease Prediction (Image Left, Text Right)
col1, col2 = st.columns([1, 2])

with col1:
    st.image("diesease_prediction.jpeg", width=300)
with col2:
    st.markdown("### 1️⃣ Disease Prediction with AI")
    st.write("""
    AI models can analyze patient symptoms, genetic data, and medical history to **predict diseases early**.  
    By identifying patterns, AI helps doctors make informed decisions and improve **early diagnosis rates**.  
    👉 [Learn more](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7179009/)
    """)

st.markdown("<hr>", unsafe_allow_html=True)

## Medicine Image Classification (Image Right, Text Left)
col3, col4 = st.columns([2, 1])

with col3:
    st.markdown("### 2️⃣ Medicine Image Classification")
    st.write("""
    AI-powered image classification helps pharmacies and hospitals **identify and categorize medicines accurately**.  
    This minimizes errors in prescription management and improves **efficiency in medical supply chains**.  
    👉 [Read more](https://medimageclassification.streamlit.app/)
    """)
with col4:
    st.image("imgae_classification.jpg", width=300)

st.markdown("<hr>", unsafe_allow_html=True)

## Predicting Outpatient Attendance (Image Left, Text Right)
col5, col6 = st.columns([1, 2])

with col5:
    st.image("outpatient.jpeg", width=300)
with col6:
    st.markdown("### 3️⃣ Predicting Outpatient Attendance")
    st.write("""
    AI can predict **hospital and clinic attendance trends** by analyzing past patient visits and seasonal changes.  
    This helps hospitals allocate **staff and resources effectively**, reducing waiting times for patients.  
    👉 [Explore AI in Healthcare](https://www.healthcareitnews.com/news/how-ai-can-improve-patient-flow-and-hospital-operations)
    """)

st.markdown("<hr>", unsafe_allow_html=True)

## Bed Occupancy Prediction (Image Right, Text Left)
col7, col8 = st.columns([2, 1])

with col7:
    st.markdown("### 4️⃣ Bed Occupancy Prediction")
    st.write("""
    AI-driven models analyze hospital data to **forecast bed demand** and **optimize hospital occupancy rates**.  
    This prevents overcrowding, improves emergency care, and ensures **better resource management**.  
    👉 [See AI's impact](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0266612)
    """)
with col8:
    st.image("bed_occupancy.jpeg", width=300)
