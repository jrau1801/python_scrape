import requests
from bs4 import BeautifulSoup
import re



def scrape_links():
    url = "https://www.kanshudo.com/collections/vocab_usefulness"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        pattern = re.compile(r"^/collections/vocab_usefulness/.+")

        # Alle passenden <a>-Tags mit hrefs extrahieren
        links = soup.find_all("a", href=pattern)

        with open("links.txt", "w", encoding="utf-8") as f:
            for link in links:
                full_url = "https://www.kanshudo.com" + link["href"]
                f.write(full_url + "\n")
            
    else:
        print("Failed to fetch page:", response.status_code)


if __name__ == '__main__':
    scrape_links()