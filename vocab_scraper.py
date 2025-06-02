import requests
from bs4 import BeautifulSoup
from bs4 import NavigableString



def scrape_vocab_once():
    url = "https://www.kanshudo.com/collections/vocab_usefulness/UFN-1-1"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    id = "115002"

    response = requests.get(url, headers=headers)
    
    soup = BeautifulSoup(response.text, "html.parser")

    jukugo_wrapper = soup.find("div", id=f"jukugo_{id}")



    # SYMBOLS
    #
    #

    jap_span = jukugo_wrapper.find("span", id=f"jk_jk_{id}_fc")

    print(jap_span)

    #
    #
    #


    

    # TRANSLATIONS
    #
    #

    vm_divs = jukugo_wrapper.find_all("div", class_="vm")

    print(', '.join(
        ''.join(child.strip() for child in div.contents if isinstance(child, NavigableString) and child.strip())
        for div in vm_divs
    ))
    
    #
    #
    #




        
        
def scrape_vocab_all_one_link():
    pass


def scrape_vocab_all_links():
    pass


if __name__ == '__main__':
    scrape_vocab_once()