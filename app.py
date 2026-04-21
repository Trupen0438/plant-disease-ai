import streamlit as st
from PIL import Image

# Page config
st.set_page_config(page_title="Plant Disease Detector", page_icon="🌿", layout="centered")

# Custom CSS for better UI
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .title {
        font-size: 36px;
        font-weight: bold;
        color: #2c7a7b;
        text-align: center;
    }
    .subtitle {
        font-size: 18px;
        text-align: center;
        color: #555;
    }
    .result-box {
        padding: 15px;
        border-radius: 10px;
        background-color: #e6fffa;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="title">🌿 AI Plant Disease Detection</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Upload a leaf image to detect disease and get treatment suggestions</p>', unsafe_allow_html=True)

st.write("")

# Upload section
uploaded_file = st.file_uploader("📤 Upload Leaf Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.image(image, caption="🖼️ Uploaded Image", use_column_width=True)

    if st.button("🔍 Analyze"):
        # TEMP (will replace with model later)
        st.markdown('<div class="result-box">', unsafe_allow_html=True)

        st.success("🌱 Disease Detected: Leaf Spot")
        st.info("📊 Prediction Strength: High")

        st.markdown("### 💊 Suggested Treatment")
        st.write("""
        - Apply neem oil spray  
        - Remove infected leaves  
        - Avoid overwatering  
        - Ensure proper sunlight  
        """)

        st.markdown('</div>', unsafe_allow_html=True)
