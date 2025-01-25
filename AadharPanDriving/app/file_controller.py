import os
from flask import request, jsonify
from app.scripts.inference import detect_features
from app.scripts.ocr import extract_text
from app.scripts.validation import verhoeff_check, validate_pan, validate_dl

def upload():
    """
    Handle file upload, perform detection, OCR, and validation.
    
    Returns:
        Response (JSON): Detection, OCR, and validation results.
    """
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'})
    
    file = request.files['file']
    document_type = request.form.get('document_type')  # Get document type from form
    search_name = request.form.get('search_name', '')  # Get search_name from form (optional)

    # Ensure the 'static' directory inside 'app' exists
    static_dir = os.path.join(os.path.dirname(__file__), '../static')
    if not os.path.exists(static_dir):
        os.makedirs(static_dir)

    file_path = os.path.join(static_dir, file.filename)
    file.save(file_path)
    
    try:
        # Step 1: Detect Features
        detection_results = detect_features(file_path)

        # Print the detection results for debugging
        print("Detection Results:", detection_results)

        # Step 2: Extract Text
        # Pass the detection result to OCR, along with the search_name
        extracted_text = extract_text(file_path, document_type, search_name)

        # Print the extracted text for debugging
        print("Extracted Text:", extracted_text)

        # Step 3: Validate Data
        is_valid = None
        if detection_results == "Aadhaar Card Identified":
            aadhaar_number = extracted_text.get('Aadhaar Number', '')
            is_valid = verhoeff_check(aadhaar_number)
        elif detection_results == "PAN Card Identified":
            pan_number = extracted_text.get('PAN Number', '')
            if pan_number:
                is_valid = validate_pan(pan_number)
        elif detection_results == "Driving License Identified":
            dl_number = extracted_text.get('Driving License Number', '')
            if dl_number:
                is_valid = validate_dl(dl_number)

        response = {
            'features_detected': detection_results,
            'extracted_text': extracted_text,
            'is_valid': is_valid
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)})
