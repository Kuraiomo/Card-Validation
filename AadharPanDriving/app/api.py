
from flask import Flask, render_template
from app.file_controller import upload

app = Flask(__name__)

@app.route('/')
def index():
    """Render the main index page."""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def handle_upload():
    """Handle file upload request."""
    return upload()

if __name__ == '__main__':
    app.run(debug=True)
