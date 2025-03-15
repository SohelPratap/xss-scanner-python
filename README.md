
# XSS Scanner

This is a simple tool to scan websites for potential **Cross-Site Scripting (XSS)** vulnerabilities. The tool crawls websites, identifies potential injection points, and tests for XSS vulnerabilities.

## 🚀 Setup Instructions

### 1. Clone the Repository
First, clone this repository to your local machine:
```bash
git clone https://github.com/SohelPratap/xss-scanner-python.git
cd xss-scanner-python
```

2. Install Dependencies

Backend (Python)
	•	Create and activate a virtual environment:

# If you don't have a virtual environment, create one
```bash
python3 -m venv xssenv
```

# Activate the virtual environment
```bash
source xssenv/bin/activate  # On Windows: xssenv\Scripts\activate
```
•	Install the required Python libraries:
```bash
pip install -r requirements.txt
```

	•	Required libraries:
	•	requests
	•	flask
	•	beautifulsoup4
	•	flask_cors

Frontend (JavaScript)
	•	Ensure you have Node.js installed for the frontend (if you decide to extend it).
	•	Frontend is written in HTML, CSS, and JavaScript, no special setup is required for running locally.

⸻

🛠️ Running the Application

1. Start the Backend Server

In the project directory, run the Flask server:
```bash
python backend/app.py
```

This will start the backend server at http://127.0.0.1:5000.

2. Start the Frontend

To run the frontend, use Python’s HTTP server to serve the HTML files:

# Navigate to the frontend folder
```bash
cd frontend
```

# Start the server
```bash
python3 -m http.server 8000
```

The frontend will be accessible at http://127.0.0.1:8000.

⸻

🧑‍💻 Using the Scanner
	1.	Open http://127.0.0.1:8000 in your browser.
	2.	Step 1: Crawl: Enter a website URL in the input field and click Step 1: Crawl. The tool will crawl the website and display found forms and links.
	3.	Step 2: Identify: Click Step 2: Identify to identify the potential XSS injection points in the website.
	4.	Step 3: Test: Click Step 3: Test to inject test payloads into the identified endpoints to check for vulnerabilities.

⸻

🧩 Contributing

Feel free to fork the repository and create a pull request. Contributions are welcome! Here’s how you can contribute:
	1.	Fork the repository.
	2.	Create a new branch (git checkout -b feature-name).
	3.	Make your changes and commit them (git commit -m 'Add feature').
	4.	Push to your branch (git push origin feature-name).
	5.	Open a pull request.

⸻

📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

⸻

🔧 Troubleshooting

Common Issues:
	•	CORS errors: Make sure that the frontend is able to access the backend by running both servers locally.
	•	Missing dependencies: Ensure all dependencies are installed using pip install -r requirements.txt for the backend.

For any other issues, please open an issue on GitHub or reach out via email.

