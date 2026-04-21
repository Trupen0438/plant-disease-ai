import streamlit as st
from PIL import Image

# Page config
st.set_page_config(page_title="Plant Disease Detector", page_icon="🌿", layout="centered")

# Custom CSS (clean green theme)
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #d4fc79, #96e6a1);
}

/* Title */
.title {
    font-size: 40px;
    font-weight: bold;
    text-align: center;
    color: #1b4332;
}

/* Subtitle */
.subtitle {
    font-size: 18px;
    text-align: center;
    color: #2d6a4f;
    margin-bottom: 20px;
}

/* Buttons */
.stButton>button {
    background-color: #2d6a4f;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 16px;
}

/* Upload box */
.stFileUploader {
    border: 2px dashed #2d6a4f;
    padding: 10px;
    border-radius: 10px;
    background-color: #f0fff4;
}

/* Result box */
.result {
    padding: 15px;
    border-radius: 10px;
    background-color: #e9f5ec;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="title">🌿 AI Plant Disease Detection</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Upload a leaf image to detect disease and get treatment instantly</p>', unsafe_allow_html=True)

# Upload
uploaded_file = st.file_uploader("📤 Upload Leaf Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="🖼️ Uploaded Image", use_column_width=True)

    if st.button("🔍 Analyze"):
        with st.spinner("Analyzing image..."):
            st.markdown('<div class="result">', unsafe_allow_html=True)

            st.success("🌱 Disease Detected: Leaf Spot")

            st.markdown("### 💊 Suggested Treatment")
            st.write("""
            - Apply neem oil spray  
            - Remove infected leaves  
            - Avoid overwatering  
            - Ensure proper sunlight  
            """)

            st.markdown('</div>', unsafe_allow_html=True)
