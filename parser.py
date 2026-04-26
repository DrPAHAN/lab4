import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def parse_url(url: str) -> dict:
    parsed = urlparse(url)
    if not parsed.scheme:
        url = "https://" + url
        parsed = urlparse(url)
    
    if not parsed.netloc:
        raise ValueError("Invalid URL")
    
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, headers=headers, timeout=10)
    resp.raise_for_status()
    resp.encoding = resp.apparent_encoding

    soup = BeautifulSoup(resp.text, "html.parser")
    title = soup.title.string.strip() if soup.title else "No title"

    desc_tag = soup.find("meta", attrs={"name": "description"})
    description = desc_tag.get("content", "").strip() if desc_tag else ""

    text = soup.get_text(separator=" ", strip=True)

    return {
        "url": url,
        "title": title[:500],
        "description": description[:1000],
        "content_length": len(text)
    }