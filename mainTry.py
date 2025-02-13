import streamlit as st

# Custom CSS to display buttons in a single row
st.markdown("""
    <style>
        .button-container {
            display: flex;
            justify-content: center;
            gap: 20px;
            padding: 20px;
            flex-wrap: wrap;
        }
        .button-container a button {
            font-size: 18px;
            font-weight: bold;
            color: white;
            background-color: #4CAF50;
            padding: 12px 24px;
            border-radius: 30px;
            cursor: pointer;
            transition: background 0.3s ease, transform 0.3s ease;
            text-align: center;
            border: none;
            width: 220px;
        }
        .button-container a button:hover {
            background-color: #388E3C;
            transform: scale(1.05);
        }
    </style>
""", unsafe_allow_html=True)

# Create buttons in a single row
st.markdown('<div class="button-container">', unsafe_allow_html=True)
st.markdown('<a href="https://your-disease-prediction-deployment-link.com" target="_blank"><button>🩺 Disease Prediction</button></a>', unsafe_allow_html=True)
st.markdown('<a href="https://medimageclassification.streamlit.app/" target="_blank"><button>📸 Medicine Image Classifier</button></a>', unsafe_allow_html=True)
st.markdown('<a href="https://your-outpatient-prediction-deployment-link.com" target="_blank"><button>📅 Outpatient Prediction</button></a>', unsafe_allow_html=True)
st.markdown('<a href="https://your-bed-occupancy-deployment-link.com" target="_blank"><button>🛏 Bed Occupancy Prediction</button></a>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Homepage content
st.title("🏥 AI in Healthcare: Optimizing Resources & Accessibility")

st.image("healthcare_banner.jpg", use_container_width=True)
st.write("""
As Singapore’s healthcare system evolves, **leveraging cutting-edge technologies** becomes crucial.  
With **increasing demand** for medical services and resources, AI offers new possibilities to optimize healthcare.

> **“How can we leverage AI to optimize healthcare resources and improve accessibility for Singaporeans?”**
""")

st.subheader("🔍 How AI is Transforming Healthcare in Singapore")

# AI Applications in 2x2 Grid
col1, col2 = st.columns(2)

with col1:
    st.image("diesease_prediction.jpeg", width=300)  # Uniform size
    st.markdown("**1️⃣ Disease Prediction with AI** - AI models can analyze symptoms and predict diseases early. 👉 [Learn more](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7179009/)")

with col2:
    st.image("imgae_classification.jpg", width=300)  # Uniform size
    st.markdown("**2️⃣ Medicine Image Classification** - AI-powered recognition helps classify medicines. 👉 [Read more](https://medimageclassification.streamlit.app/)")

col3, col4 = st.columns(2)

with col3:
    st.image("outpatient.jpeg", width=300)  # Uniform size
    st.markdown("**3️⃣ Predicting Outpatient Attendance** - AI can forecast patient volume. 👉 [Explore AI in Healthcare](https://www.healthcareitnews.com/news/how-ai-can-improve-patient-flow-and-hospital-operations)")

with col4:
    st.image("bed_occupancy.jpeg", width=300)  # Uniform size
    st.markdown("**4️⃣ Bed Occupancy Prediction** - AI predicts hospital bed demand.  👉 [See AI's impact](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0266612)")
