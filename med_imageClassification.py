import streamlit as st

# Custom CSS for styling
st.markdown("""
    <style>
        .main-container {
            padding: 30px;
            max-width: 1000px;
            margin: auto;
        }
        .header {
            text-align: center;
            font-size: 26px;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .sub-header {
            font-size: 22px;
            font-weight: bold;
            margin-top: 30px;
        }
        .text {
            font-size: 16px;
            line-height: 1.6;
            text-align: justify;
        }
        .image-container {
            text-align: center;
            margin: 20px 0;
        }
        .link {
            color: #4CAF50;
            font-weight: bold;
            text-decoration: none;
        }
        .link:hover {
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-container">', unsafe_allow_html=True)

st.image("healthcare_banner.jpg", use_column_width=True)

st.markdown('<div class="header">🏥 AI in Healthcare: Optimizing Resources & Accessibility</div>', unsafe_allow_html=True)

st.markdown("""
    <p class="text">
    As Singapore’s healthcare system evolves, <b>leveraging cutting-edge technologies</b> is crucial to address emerging challenges. 
    With increasing demand for medical services and resources, traditional approaches may no longer suffice.
    <br><br>
    However, <b>Artificial Intelligence (AI)</b> offers solutions to enhance efficiency in hospitals, optimize healthcare resources, and 
    improve accessibility. This leads us to our <b>problem statement</b>:
    </p>
""", unsafe_allow_html=True)

st.markdown('<p class="sub-header">“How can we leverage AI to optimize healthcare resources and improve accessibility for Singaporeans?”</p>', unsafe_allow_html=True)

# AI Applications Section
st.markdown('<div class="sub-header">🔍 How AI is Transforming Healthcare</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.image("diesease_prediction.jpeg", use_column_width=True)
    st.markdown("""
    **1️⃣ Disease Prediction with AI**  
    AI models can analyze symptoms and predict possible diseases early, improving diagnostic efficiency.  
    👉 <a class="link" href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7179009/" target="_blank">Learn more</a>
    """, unsafe_allow_html=True)

with col2:
    st.image("imgae_classification.jpg", use_column_width=True)
    st.markdown("""
    **2️⃣ Medicine Image Classification**  
    AI-powered image recognition can help classify medicines, reducing prescription errors and enhancing pharmaceutical management.  
    👉 <a class="link" href="https://www.frontiersin.org/articles/10.3389/fphar.2021.700569/full" target="_blank">Read about AI in Pharma</a>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)  # Add spacing

col3, col4 = st.columns(2)

with col3:
    st.image("outpatient.jpeg", use_column_width=True)
    st.markdown("""
    **3️⃣ Predicting Outpatient Attendance**  
    AI can forecast patient volume at clinics and hospitals, allowing better staffing and resource allocation.  
    👉 <a class="link" href="https://www.healthcareitnews.com/news/how-ai-can-improve-patient-flow-and-hospital-operations" target="_blank">Explore AI in Healthcare Operations</a>
    """, unsafe_allow_html=True)

with col4:
    st.image("bed_occupancy.jpeg", use_column_width=True)
    st.markdown("""
    **4️⃣ Bed Occupancy Prediction**  
    AI can predict hospital bed demand, helping optimize patient flow and reducing waiting times.  
    👉 <a class="link" href="https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0266612" target="_blank">See AI's impact on bed management</a>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)  # Add spacing

# Conclusion Section
st.markdown("""
    <div class="sub-header">🚀 The Future of AI in Healthcare</div>
    <p class="text">
    AI-driven healthcare solutions can lead to <b>more efficient hospitals, improved patient care, and better resource utilization</b>. 
    With continuous advancements, AI will play a critical role in shaping <b>Singapore’s future healthcare landscape</b>.
    <br><br>
    Navigate through the sidebar to explore different AI models in action! 💡
    </p>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # End main container
