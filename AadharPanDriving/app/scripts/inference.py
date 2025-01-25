import torch
import cv2
from pathlib import Path
from ultralytics import YOLO
import pandas as pd  # Ensure this is installed

# Load YOLO model
model = YOLO('app\models\Aadhar.pt')

def detect_features(image_path):
    try:
        # Read the input image
        img = cv2.imread(image_path)
        if img is None:
            raise FileNotFoundError(f"Image not found at {image_path}")
        
        # Perform detection
        results = model(image_path)  # Directly pass the path for inference
        
        # Ensure output directory exists
        output_dir = Path(r'C:\Users\ayaan\OneDrive\Desktop\AADHARPANDRIVING\app\static\output')
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Render and save detected images
        for i, result in enumerate(results):
            # Render bounding boxes on image
            annotated_image = result.plot()
            output_path = output_dir / f"output_{i}.jpg"
            cv2.imwrite(str(output_path), annotated_image)
        
        # Convert detection results to Pandas DataFrame
        detection_df = pd.DataFrame(
            results[0].boxes.data.cpu().numpy(),
            columns=['x1', 'y1', 'x2', 'y2', 'confidence', 'class']
        )
        
        # Confidence Threshold Check
        if detection_df.empty or (detection_df['confidence'] < 0.8).all():
            return "Document Not Identified"
        
        # Map class indices to document types
        class_map = {0: "Aadhaar Card" ,1:"Driving License",2:"PAN Card"}
        
        # Find the highest confidence detection
        top_detection = detection_df.iloc[detection_df['confidence'].idxmax()]
        detected_class = int(top_detection['class'])
        
        # Return the corresponding document type
        return f"{class_map.get(detected_class, 'Unknown Document')} Identified"

    except Exception as e:
        print(f"Error in detect_features: {e}")
        return None
