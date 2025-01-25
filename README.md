# Card-Validation

## Introduction

This project provides a comprehensive API for document processing, including file uploads, feature detection, optical 
character recognition (OCR), and data validation. The API is designed to process Aadhaar cards, PAN cards, and Driving 
Licenses, performing tasks like extracting text and validating details.

## Getting Started

To set up and use the project on your local system, follow these steps:

### Installation Process
1.  Clone the repository:
    git clone https://github.com/Kuraiomo/Card-Validation/tree/main/AadharPanDriving
    cd AadharPanDriving
2. Install required Python packages:
    Install required Python packages:

### Software Dependencies

* Python 3.8 or higher

* Flask

* OpenCV

* EasyOCR

* Pandas

* PyTorch

* ultralytics

### API References
Refer to the api.py file for detailed API endpoint descriptions.

### Build and Test
Run the Flask application:
    python run.py
Access the application at http://127.0.0.1:5000/ in your browser.
### Testing
To test the application:
1. Use tools like Postman or Curl to send HTTP requests to the /upload endpoint.
2. Include a file and required form data (e.g., document_type, search_name).
3. Validate responses for feature detection, text extraction, and data validation.

### Contribute
We welcome contributions to improve this project. Follow these steps to contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix:
    git checkout -b feature/your-feature-name
3. Commit your changes:
    git commit -m "Add feature or fix description"
Push your branch:
    git push origin feature/your-feature-name
Submit a pull request.


