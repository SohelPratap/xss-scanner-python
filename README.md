
---

# XSS Scanner

A simple tool to scan websites for potential **Cross-Site Scripting (XSS)** vulnerabilities. This tool crawls websites, identifies injection points, and tests for XSS vulnerabilities.

---

## 🚀 Setup Instructions

### 1. Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/SohelPratap/xss-scanner-python.git
cd xss-scanner-python
```

### 2. Install Dependencies

#### Backend (Python)
- Create and activate a virtual environment:
  ```bash
  python3 -m venv xssenv
  source xssenv/bin/activate  # On Windows: xssenv\Scripts\activate
  ```
- Install required Python libraries:
  ```bash
  pip install -r requirements.txt
  ```
- Required libraries:
  - `requests`
  - `flask`
  - `beautifulsoup4`
  - `flask_cors`

#### Frontend (JavaScript)
- Ensure **Node.js** is installed (optional, for future extensions).
- The frontend uses HTML, CSS, and JavaScript—no special setup needed for local use.

---

## 🛠️ Running the Application

### Start the Backend Server
In the project directory, run the Flask server:
```bash
python backend/app.py
```
- Backend will run at `http://127.0.0.1:5000`.

### Start the Frontend
Navigate to the `frontend` folder and serve the HTML files:
```bash
cd frontend
python3 -m http.server 8000
```
- Frontend will be accessible at `http://127.0.0.1:8000`.

---

## 🧑‍💻 Using the Scanner
1. Open `http://127.0.0.1:8000` in your browser.
2. **Step 1: Crawl**  
   - Enter a website URL and click "Step 1: Crawl."  
   - The tool will crawl the site and display forms and links.
3. **Step 2: Identify**  
   - Click "Step 2: Identify" to find potential XSS injection points.
4. **Step 3: Test**  
   - Click "Step 3: Test" to inject payloads and check for vulnerabilities.

---

## 🧩 Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add feature'
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## 📄 License
This project is licensed under the [MIT License](LICENSE).

---

## 🔧 Troubleshooting
- **CORS Errors**: Ensure the frontend and backend are running locally.
- **Missing Dependencies**: Run `pip install -r requirements.txt` to install all backend dependencies.
- For other issues, open a GitHub issue or email the maintainer.

---

