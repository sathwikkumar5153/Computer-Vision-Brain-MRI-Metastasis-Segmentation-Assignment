import cv2
import numpy as np
import albumentations as A

def apply_clahe(image):
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    return clahe.apply(image)

def preprocess_image(image, mask):
    # Apply CLAHE
    image = apply_clahe(image)
    
    # Normalize
    image = image / 255.0
    
    # Augmentations
    transform = A.Compose([
        A.HorizontalFlip(p=0.5),
        A.VerticalFlip(p=0.5),
        A.RandomRotate90(p=0.5),
        A.ShiftScaleRotate(shift_limit=0.0625, scale_limit=0.1, rotate_limit=45, p=0.5),
    ])
    
    transformed = transform(image=image, mask=mask)
    return transformed['image'], transformed['mask']