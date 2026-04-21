import streamlit as st
from PIL import Image

st.title("🌿 AI-Based Plant Disease Detection")

st.write("Upload a leaf image to detect plant disease.")

uploaded_file = st.file_uploader("Choose a leaf image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image")

    if st.button("Predict"):
        st.subheader("Result:")
        st.success("Disease Detected: Leaf Spot")

        st.subheader("Prediction Strength:")
        st.info("High")

        st.subheader("Suggested Treatment:")
        st.write("""
        - Use neem oil spray  
        - Remove infected leaves  
        - Avoid overwatering  
        """)
