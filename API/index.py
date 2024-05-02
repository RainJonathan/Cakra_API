from flask import Flask, request, jsonify
from controller.summerizer import generate_summary

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Worlds!'

@app.route('/about')
def about():
    return 'About'

@app.route('/post_example', methods=['POST'])
def post_example():
    # Access request data
    data = request.json  # assuming JSON data is sent
    # Select the content of the "payload" field
    payload_content = data.get('payload', '')  # If "payload" key doesn't exist, default to empty string
    # Process the data
    processed_data = generate_summary(payload_content)
    # Return a response
    return jsonify({'error':False, 'message': 'Data Processed Succesfully', 'processed_data': processed_data})

if __name__ == '__main__':
    app.run(debug=True)
