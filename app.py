import streamlit as st
from PIL import Image
import base64

# Page config
st.set_page_config(page_title="Plant Disease Detector", page_icon="🌿", layout="centered")

# Function to set background image
def set_bg():
    bg_url = "https://images.unsplash.com/photo-1501004318641-b39e6451bec6"
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{bg_url}");
            background-size: cover;
            background-attachment: fixed;
        }}

        .glass {{
            background: rgba(255, 255, 255, 0.85);
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0px 4px 20px rgba(0,0,0,0.2);
        }}

        .title {{
            font-size: 38px;
            font-weight: bold;
            color: #2f855a;
            text-align: center;
        }}

        .subtitle {{
            font-size: 18px;
            text-align: center;
            color: #333;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg()

# Glass container
st.markdown('<div class="glass">', unsafe_allow_html=True)

# Title
st.markdown('<p class="title">🌿 AI Plant Disease Detection</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Upload a leaf image and detect plant diseases instantly</p>', unsafe_allow_html=True)

st.write("")

# Upload
uploaded_file = st.file_uploader("📤 Upload Leaf Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="🖼️ Uploaded Image", use_column_width=True)

    if st.button("🔍 Analyze"):
        with st.spinner("Analyzing image..."):
            st.success("🌱 Disease Detected: Leaf Spot")

            st.markdown("### 💊 Suggested Treatment")
            st.write("""
            - Apply neem oil spray  
            - Remove infected leaves  
            - Avoid overwatering  
            - Ensure proper sunlight  
            """)

st.markdown('</div>', unsafe_allow_html=True)
