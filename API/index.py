from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS class

from controller.summerizer import generate_summary
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def home():
    return 'Hello, World!'  # Corrected typo in return statement

@app.route('/about')
def about():
    return 'About'

@app.route('/summarize', methods=['POST'])  # Corrected typo in route URL
def post_example():
    # Access request data
    data = request.json  # assuming JSON data is sent
    # Select the content of the "payload" field
    payload_content = data.get('payload', '')  # If "payload" key doesn't exist, default to empty string
    # Process the data
    processed_data = generate_summary(payload_content)
    # Return a response
    return jsonify({'error': False, 'message': 'Data Processed Successfully', 'processed_data': processed_data})

if __name__ == '__main__':
    app.run(debug=True)
