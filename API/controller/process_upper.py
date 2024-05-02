# data_processing.py

def process_data(data):
    # Extract the "payload" from the data and convert it to uppercase
    payload = data.get('payload', '')
    processed_payload = payload.upper()
    return processed_payload
