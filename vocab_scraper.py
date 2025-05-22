import requests
from bs4 import BeautifulSoup



def scrape_vocab_once():
    url = "https://www.kanshudo.com/collections/vocab_usefulness/UFN-1-1"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    
    soup = BeautifulSoup(response.text, "html.parser")

    if response.status_code == 200:
        jukugo_wrapper = soup.find("div", id="jukugo_115002")
        print(jukugo_wrapper)
            
    else:
        print("Failed to fetch page:", response.status_code)
        
        
def scrape_vocab_all_one_link():
    pass


def scrape_vocab_all_links():
    pass


if __name__ == '__main__':
    scrape_vocab_once()