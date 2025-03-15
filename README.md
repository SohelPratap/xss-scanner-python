

---

# XSS Scanner (Python)

A Python-based tool to detect Cross-Site Scripting (XSS) vulnerabilities in web applications by scanning input fields and analyzing responses.

## Features
- Scans for reflected and stored XSS
- Customizable payloads
- Command-line interface
- Detailed reporting

## Prerequisites
- Python 3.x
- Dependencies: `requests`, `beautifulsoup4` (install via `pip`)

## Installation
```bash
git clone https://github.com/SohelPratap/xss-scanner-python.git
cd xss-scanner-python
pip install -r requirements.txt
```

## Usage
```bash
python xss_scanner.py -u <target_url> [-p payloads.txt] [-o output.txt]
```
- `-u`: Target URL (required)
- `-p`: Custom payload file (optional)
- `-o`: Output file (optional)

**Example:**
```bash
python xss_scanner.py -u "http://example.com" -o results.txt
```

## Output
```
[XSS Scanner]
Target: http://example.com
Found: 1 vuln (search param - Reflected XSS)
Saved to: results.txt
```

## Contributing
Fork, branch, commit, and submit a PR. All contributions welcome!

## Disclaimer
For educational use and authorized testing only. Not responsible for misuse.

## License
[MIT License](LICENSE)

## Contact
- GitHub: [SohelPratap](https://github.com/SohelPratap)

---

