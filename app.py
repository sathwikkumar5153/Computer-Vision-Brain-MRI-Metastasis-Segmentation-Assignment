from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import torch
from PIL import Image
import numpy as np
from your_best_model import BestModel

app = FastAPI()

model = BestModel()
model.load_state_dict(torch.load('best_model.pth'))
model.eval()

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = Image.open(file.file)
    # Preprocess image
    # Make prediction
    # Post-process result
    return JSONResponse(content={"result": result})