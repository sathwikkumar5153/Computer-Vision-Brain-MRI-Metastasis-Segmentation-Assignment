import streamlit as st
import requests
from PIL import Image
import io

st.title("Brain MRI Metastasis Segmentation")

uploaded_file = st.file_uploader("Choose a brain MRI image", type="tif")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded MRI Image', use_column_width=True)
    
    if st.button('Predict'):
        files = {"file": uploaded_file.getvalue()}
        response = requests.post("http://localhost:8000/predict", files=files)
        result = response.json()
        
        # Display result
        st.image(result['segmentation'], caption='Segmentation Result', use_column_width=True)