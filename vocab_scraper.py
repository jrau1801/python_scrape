import requests
from bs4 import BeautifulSoup
from bs4 import NavigableString



def scrape_vocab_once(url, headers):

    id = "115002"

    response = requests.get(url, headers=headers)
    
    soup = BeautifulSoup(response.text, "html.parser")



    jukugo_wrapper = soup.find("div", id=f"jukugo_{id}")



    # SYMBOLS
    #
    #

    jap_span = jukugo_wrapper.find("span", id=f"jk_jk_{id}_fc")

    for div in jap_span:
        print(div)

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




def scrape_with_spaces():
    url = "https://www.kanshudo.com/collections/vocab_usefulness/UFN-1-101"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    #id = "326530"  # no text
    #id = "99913" # no space
    id = "266088"  # with space

    response = requests.get(url, headers=headers)
    
    soup = BeautifulSoup(response.text, "html.parser")



    jukugo_wrapper = soup.find("div", id=f"jukugo_{id}")



    # SYMBOLS
    #
    #

    a_tag = jukugo_wrapper.find("a", id=f"jk_{id}")

    jap_span = a_tag.find_all("span", id=f"jk_jk_{id}_fc")


    furigana = ""
    kanji = ""

    for span in jap_span:
        for div in span:
            class_list = div.get("class", [])

            if "furigana" in class_list:
                furigana = furigana + div.get_text(strip=True)
    
            elif "f_kanji" in class_list:
                kanji = kanji + div.get_text(strip=True)

    if furigana == "":
        print(a_tag.text)
    else:
        print(furigana)
        print(kanji)

    #
    #
    #

        
def scrape_vocab_all_one_link():
    pass


def scrape_vocab_all_links():
    pass


if __name__ == '__main__':
    url = "https://www.kanshudo.com/collections/vocab_usefulness/UFN-1-1"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    #scrape_vocab_once(url, headers)
    scrape_with_spaces()