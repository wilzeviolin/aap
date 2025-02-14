import streamlit as st

# Set the page layout to wide
st.set_page_config(layout="wide")

# Enhanced CSS for better spacing and alignment
st.markdown("""
    <style>
        /* Improved text styling */
        .full-width-text {
            text-align: justify;
            font-size: 18px;
            line-height: 1.6;
            margin-bottom: 2rem;
        }
        
        /* Container for better alignment */
        .content-container {
            display: flex;
            align-items: center;
            gap: 0;
            margin: 1rem 0;
        }
        
        /* Right-aligned image container */
        .image-right {
            display: flex;
            justify-content: flex-end;
            margin-left: auto;
            padding: 0;
        }
        
        /* Left-aligned image container */
        .image-left {
            display: flex;
            justify-content: flex-start;
            margin-right: auto;
            padding: 0;
        }
        
        /* Text content styling */
        .text-content {
            flex: 1;
            padding-right: 2rem;
        }
        
        /* Section divider */
        .section-divider {
            margin: 2rem 0;
            border-top: 1px solid #e5e5e5;
        }
        
        /* Heading styles */
        h1, h2, h3 {
            color: #2c3e50;
            margin-bottom: 1rem;
        }
        
        /* Link styling */
        a {
            color: #3498db;
            text-decoration: none;
            font-weight: 500;
        }
        
        a:hover {
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

# Page title and banner
st.title("🏥 AI in Healthcare: Optimizing Resources & Accessibility")
st.image("healthcare_banner.jpg", use_column_width=True)

# Introduction section
st.markdown("""
    <div class="full-width-text">
        As Singapore's healthcare system evolves, <b>leveraging cutting-edge technologies</b> becomes crucial.
        With the nation's <b>aging population and increasing demand</b> for medical services, AI provides an opportunity to optimize healthcare delivery.
        <b>AI-driven solutions</b> are helping in disease prediction, outpatient management, and resource allocation, ensuring that patients receive the care they need efficiently.
        By integrating AI, healthcare providers can reduce bottlenecks, improve diagnostics, and enhance the patient experience.
        <b>How can AI help optimize healthcare resources and improve accessibility for Singaporeans?</b>
    </div>
""", unsafe_allow_html=True)

st.subheader("🔍 How AI is Transforming Healthcare in Singapore")

# Content sections using custom columns
# 1. Disease Prediction
col1, col2 = st.columns([2, 1], gap="small")
with col1:
    st.markdown("""
        ### 1️⃣ Disease Prediction with AI
        AI models can analyze patient symptoms, genetic data, and medical history to **predict diseases early**.
        By identifying patterns, AI helps doctors make informed decisions and improve **early diagnosis rates**.
        👉 [Learn more](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7179009/)
    """)
with col2:
    st.markdown('<div class="image-right">', unsafe_allow_html=True)
    st.image("diesease_prediction.jpeg", width=300)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# 2. Medicine Image Classification
col3, col4 = st.columns([1, 2], gap="small")
with col3:
    st.image("imgae_classification.jpg", width=300)
with col4:
    st.markdown("""
        ### 2️⃣ Medicine Image Classification
        AI-powered image classification helps pharmacies and hospitals **identify and categorize medicines accurately**.
        This minimizes errors in prescription management and improves **efficiency in medical supply chains**.
        👉 [Read more](https://medimageclassification.streamlit.app/)
    """)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# 3. Predicting Outpatient Attendance
col5, col6 = st.columns([2, 1], gap="small")
with col5:
    st.markdown("""
        ### 3️⃣ Predicting Outpatient Attendance
        AI can predict **hospital and clinic attendance trends** by analyzing past patient visits and seasonal changes.
        This helps hospitals allocate **staff and resources effectively**, reducing waiting times for patients.
        👉 [Explore AI in Healthcare](https://www.healthcareitnews.com/news/how-ai-can-improve-patient-flow-and-hospital-operations)
    """)
with col6:
    st.markdown('<div class="image-right">', unsafe_allow_html=True)
    st.image("outpatient.jpeg", width=300)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# 4. Bed Occupancy Prediction
col7, col8 = st.columns([1, 2], gap="small")
with col7:
    st.image("bed_occupancy.jpeg", width=300)
with col8:
    st.markdown("""
        ### 4️⃣ Bed Occupancy Prediction
        AI-driven models analyze hospital data to **forecast bed demand** and **optimize hospital occupancy rates**.
        This prevents overcrowding, improves emergency care, and ensures **better resource management**.
        👉 [See AI's impact](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0266612)
    """)
