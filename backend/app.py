import os
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from crawl import crawl_website
from payloadcheck import check_for_xss
from identifyvul import process_injection_points

app = Flask(__name__)
CORS(app)

RESULTS_DIR = "dynamicresult"

def save_to_file(filename, data):
    """ Save JSON data to a text file (overwrite each time). """
    filepath = os.path.join(RESULTS_DIR, filename)
    try:
        os.makedirs(RESULTS_DIR, exist_ok=True)  # Ensure directory exists
        with open(filepath, "w") as file:
            json.dump(data, file, indent=4)
        print(f"✅ Successfully saved {filename} with {len(data.get('forms', []))} forms and {len(data.get('queryParams', {}))} query parameters.")
    except Exception as e:
        print(f"❌ Error saving {filename}: {e}")

def read_file(filename):
    """ Read JSON data from a text file. """
    filepath = os.path.join(RESULTS_DIR, filename)
    if not os.path.exists(filepath):
        return None
    with open(filepath, "r") as file:
        return json.load(file)

@app.route("/crawl", methods=["POST"])
def crawl():
    """ Step 1: Crawl website for endpoints with injection fields. """
    data = request.json
    url = data.get("url")

    if not url:
        return jsonify({"error": "URL is required"}), 400

    crawled_data = crawl_website(url)
    save_to_file("first.txt", crawled_data)

    # Verify data saved
    saved_data = read_file("first.txt")
    if saved_data:
        print(f"✅ Verified: first.txt contains {len(saved_data.get('forms', []))} forms and {len(saved_data.get('queryParams', {}))} query parameters.")

    return jsonify({"message": "Crawling completed.", "crawledEndpoints": crawled_data})

@app.route("/identify", methods=["POST"])
def identify():
    """ Step 2: Identify injection types and save results. """
    crawled_data = read_file("first.txt")
    if not crawled_data:
        return jsonify({"error": "No crawled data found. Run Step 1 first."}), 400

    injection_points = process_injection_points(crawled_data.get("forms", []))
    save_to_file("second.txt", injection_points)

    return jsonify({"message": "Injection points identified.", "injectionPoints": injection_points})

@app.route("/test", methods=["POST"])
def test_payloads():
    """ Step 3: Run payload testing based on identified injection points. """
    injection_points = read_file("second.txt")
    if not injection_points:
        return jsonify({"error": "No injection data found. Run Step 2 first."}), 400

    test_results = []
    for inj in injection_points:
        xss_results = check_for_xss(inj["endpoint"], inj["xss_type"])
        if xss_results:
            test_results.append({
                "endpoint": inj["endpoint"],
                "result": "Vulnerable",
                "tested_payloads": xss_results
            })

    save_to_file("third.txt", test_results)

    return jsonify({"message": "Payload testing completed.", "testResults": test_results})

if __name__ == "__main__":
    os.makedirs(RESULTS_DIR, exist_ok=True)
    app.run(debug=True, port=5000)