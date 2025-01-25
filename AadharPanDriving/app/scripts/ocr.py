
import cv2
import re
from pathlib import Path
import easyocr

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

def extract_text(image_path, document_type, search_name=None):
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Image not found at {image_path}")
        return None

    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Use EasyOCR to extract text
    text = reader.readtext(gray, detail=0)
    text = " ".join(text)  # Join extracted text into a single string

    # Check if any text is extracted
    if not text.strip():
        print("No text detected in the image.")
        return {'Extracted Text': '', 'Additional Info': ''}

    # Initialize the output dictionary with extracted text
    extracted_data = {'Extracted Text': text}

    # Check if search_name is provided, and search for it in the text
    if search_name:
        name_found = re.search(re.escape(search_name), text, re.IGNORECASE) is not None
        extracted_data['Name Found'] = name_found

    # Process based on document type and extract additional details
    if document_type == "Aadhaar Card Identified":
        aadhaar_match = re.search(r'\b\d{4}\s?\d{4}\s?\d{4}\b', text)
        aadhaar_number = aadhaar_match.group(0).replace(' ', '') if aadhaar_match else ''
        extracted_data['Aadhaar Number'] = aadhaar_number

    elif document_type == "PAN Card Identified":
        pan_match = re.search(r'\b[A-Za-z]{5}\d{4}[A-Za-z]{1}\b', text)
        pan_number = pan_match.group(0) if pan_match else ''
        extracted_data['PAN Number'] = pan_number

    elif document_type == "Driving License Identified":
        dl_match = re.search(r'\b[A-Z]{2}[0-9]{2}\s?\d{10,12}\b', text)
        dl_number = dl_match.group(0) if dl_match else ''
        extracted_data['Driving License Number'] = dl_number

    else:
        extracted_data['Additional Info'] = "Unsupported document type or generic text extraction."

    # Define the output directory and file
    output_dir = Path(r'C:\Users\ayaan\OneDrive\Desktop\AADHARPANDRIVING\app\static\output')
    output_dir.mkdir(parents=True, exist_ok=True)  # Ensure output directory exists
    output_file = output_dir / "extracted_text.txt"

    # Write the extracted text to the text file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)

    print(f"Text extracted and saved to {output_file}")
    
    return extracted_data
