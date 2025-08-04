import os, requests

CONFLUENCE_BASE_URL = os.getenv("CONFLUENCE_BASE_URL")
CONFLUENCE_API_KEY = os.getenv("CONFLUENCE_API_KEY")
CONFLUENCE_USER = os.getenv("CONFLUENCE_USER")
SPACE_KEY = os.getenv("CONFLUENCE_SPACE", "ProductDocs")
DOCS_DIR = "outputs/docs"

headers = {
    "Authorization": f"Basic {CONFLUENCE_API_KEY}",
    "Content-Type": "application/json"
}

def publish_page(title, content):
    payload = {
        "type": "page",
        "title": title,
        "space": {"key": SPACE_KEY},
        "body": {
            "storage": {
                "value": content,
                "representation": "wiki"
            }
        }
    }
    url = f"{CONFLUENCE_BASE_URL}/rest/api/content"
    response = requests.post(url, json=payload, headers=headers, auth=(CONFLUENCE_USER, CONFLUENCE_API_KEY))
    print(f"[{title}] -> {response.status_code}")

if __name__ == "__main__":
    for file in os.listdir(DOCS_DIR):
        with open(os.path.join(DOCS_DIR, file), "r") as f:
            content = f.read()
            publish_page(file.replace(".md", ""), content)
