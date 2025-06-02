import requests
from bs4 import BeautifulSoup
from bs4 import NavigableString
import re

def scrape_with_spaces():

    #url = "https://www.kanshudo.com/collections/vocab_usefulness/UFN-5-4901" #multiple spaces
    #id = "261471"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    url = "https://www.kanshudo.com/collections/vocab_usefulness/UFN-1-101"
    #id = "326530"  # no text
    #id = "99913" # no space
    id = "266088"  # with space

    response = requests.get(url, headers=headers)
    
    soup = BeautifulSoup(response.text, "html.parser")



    jukugo_wrapper = soup.find("div", id=f"jukugo_{id}")


########################################################## 

# KANJI


    a_tag = jukugo_wrapper.find("a", id=f"jk_{id}")

    onclick_attr = a_tag.get("onclick", "")

    match = re.search(r"wordDetails\([^,]+,\s*'([^']+)'", onclick_attr)

    word = ""
    if match:
        word = match.group(1)


##########################################################

# FURIGANA

    furigana = ""
    jap_span = a_tag.find_all("span", id=f"jk_jk_{id}_fc")
    furigana_parts = []
    kanji = word

    for span in jap_span:
        for div in span:
            class_list = div.get("class", [])

            if "furigana" in class_list:
                furigana_parts.append(div.get_text(strip=True))


        furigana = ', '.join(furigana_parts)


##########################################################

# TRANSLATIONS

    vm_divs = jukugo_wrapper.find_all("div", class_="vm")

    translations= ', '.join(
        ''.join(child.strip() for child in div.contents if isinstance(child, NavigableString) and child.strip())
        for div in vm_divs
    )


##########################################################

# RESULT

    if furigana == "":
        result = kanji + " | " + translations
    else: 
        result = kanji + " | " + furigana + " | " + translations

    print(result)




if __name__ == '__main__':
    url = "https://www.kanshudo.com/collections/vocab_usefulness/UFN-1-1"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    scrape_with_spaces()