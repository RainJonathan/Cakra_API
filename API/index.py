from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS class

from controller.summerizer import generate_summary

from controller.language import EasyGoogleTranslate
from langdetect import detect
import re


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def home():
    return 'Hello, World!'  # Corrected typo in return statement

@app.route('/about')
def about():
    return 'About'

@app.route('/translate')
def translate():
    translator = EasyGoogleTranslate()
    text = 'Hello, i am your student. Do you want to play football?'
    result = translator.translate(text, target_language='id')
    detected_language = (detect(result))
    detected_language = re.sub(r'(?<=-)([a-z]+)', lambda x: x.group(0).upper(), detected_language)
    print(detected_language)

    print(translator.translate(text, target_language=detected_language))
    return jsonify({'error': False, 'message': 'Data Processed Successfully', 'processed_data': translator.translate(text, target_language=detected_language)})

@app.route('/summarize', methods=['POST'])  # Corrected typo in route URL
def summarize():
    data = request.json  # assuming JSON data is sent
    # Select the content of the "payload" field
    payloads = data.get('payload', [])  # If "payload" key doesn't exist, default to empty list
    processed_data = []

    # Process the data
    for payload_content in payloads:
        translator = EasyGoogleTranslate()
        text = payload_content.get('text', '')

        first_result = translator.translate(text, target_language='en') # Get the text from each payload object

        summary = generate_summary(first_result)

        detected_language = (detect(text))
        detected_language = re.sub(r'(?<=-)([a-z]+)', lambda x: x.group(0).upper(), detected_language)
        print(detected_language)

        final_result = translator.translate(summary, target_language=detected_language)
        processed_data.append(final_result)
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    print(f"Request received from IP: {client_ip}")

    # Return a response
    return jsonify({'error': False, 'message': 'Data Processed Successfully', 'processed_data': processed_data})

if __name__ == '__main__':
    app.run(debug=True)



