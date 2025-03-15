import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, parse_qs

def crawl_website(url):
    """ Crawls a website to find forms and query parameters. """
    headers = {
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
      }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Debugging: Print full HTML response (truncated)
        print(f"\n🔍 HTML Content of {url}:\n", soup.prettify()[:1000], "\n... (truncated)")

        links = [urljoin(url, a["href"]) for a in soup.find_all("a", href=True)]
        print(f"🔗 Extracted Links: {links}")

        query_params = {}
        for link in links:
            parsed_url = urlparse(link)
            if parsed_url.query:
                query_params[link] = list(parse_qs(parsed_url.query).keys())

        forms = []
        for form in soup.find_all("form"):
            action = urljoin(url, form.get("action", url))
            inputs = [{"name": inp.get("name", ""), "type": inp.get("type", "text")} for inp in form.find_all("input")]
            print(f"📝 Found Form - Action: {action}, Inputs: {inputs}")

            if inputs:
                forms.append({"action": action, "inputs": inputs})

        return {"queryParams": query_params, "forms": forms}
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return {"error": str(e)}