Brain MRI Metastasis Segmentation Project
Project Overview
This project implements and compares Nested U-Net (U-Net++) and Attention U-Net architectures for brain MRI metastasis segmentation. It includes a web application to demonstrate the model's capabilities.
Key Features

Implementation of Nested U-Net and Attention U-Net for metastasis segmentation
CLAHE preprocessing for enhanced metastasis visibility
Data augmentation techniques specific to medical imaging
FastAPI backend for model serving
Streamlit UI for easy interaction with the segmentation model

Installation Instructions

Clone the repository:
Copygit clone https://github.com/yourusername/brain-mri-segmentation.git
cd brain-mri-segmentation

Create a virtual environment:
Copypython -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install required packages:
Copypip install -r requirements.txt

Download the dataset:
Copy# Add instructions for downloading and placing the dataset


Usage Instructions

Prepare the dataset:
Copypython prepare_data.py

Train the models:
Copypython train.py

Evaluate the models:
Copypython evaluate.py

Run the FastAPI backend:
Copyuvicorn app:app --reload

Launch the Streamlit UI:
Copystreamlit run streamlit_app.py


Model Architectures Explanation
Nested U-Net (U-Net++)
Nested U-Net, also known as U-Net++, is an advanced version of the original U-Net architecture. It introduces dense skip connections and deep supervision to improve segmentation accuracy.
Key features:

Dense skip connections between encoder and decoder
Deep supervision for improved gradient flow
Better feature reuse across different scales

Attention U-Net
Attention U-Net incorporates attention gates in the skip connections of the U-Net architecture. This allows the model to focus on relevant features and suppress irrelevant ones.
Key features:

Attention gates in skip connections
Improved feature selection
Better handling of multi-scale features


Contributors

SATHWIK KUMAR RUDROJU
