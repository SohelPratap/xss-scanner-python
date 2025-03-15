import os
import requests

PAYLOADS_DIR = "payloads"

def load_payloads(file_name):
    """ Loads XSS payloads from the specified file. """
    file_path = os.path.join(PAYLOADS_DIR, file_name)
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, "r") as file:
            return [line.strip() for line in file.readlines()]
    except Exception as e:
        return []

def inject_payload(url, params, payload):
    """
    Injects payload into the parameters of the request and sends it.
    """
    try:
        test_params = {key: payload for key in params}
        response = requests.get(url, params=test_params, timeout=5)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def check_for_xss(endpoint, input_type):
    payload_files = {
        "text": "input_xss.txt",
        "url": "url_xss.txt",
        "attribute": "attribute_xss.txt",
        "js": "js_xss.txt",
        "css": "css_xss.txt",
        "dom": "dom_xss.txt"
    }

    selected_payloads = load_payloads(payload_files.get(input_type, "input_xss.txt"))
    print(f"Testing {endpoint} with {len(selected_payloads)} payloads")  # Debugging line
    
    vulnerabilities = []
    for payload in selected_payloads:
        injected_response = inject_payload(endpoint, ["test"], payload)
        if payload in injected_response:
            vulnerabilities.append(payload)
    
    return vulnerabilities