import requests
from bs4 import BeautifulSoup
from bs4 import NavigableString
import re

def scrape():

########################################################## 

# READ AND WRITE FILES


    links = []

    with open("links.txt", "r", encoding="utf-8") as file:
        links = [line.strip() for line in file if line.strip()]

    with open("vocab.txt", "a", encoding="utf-8") as f:
        f.write("#separator: tab\n#html:true\n")


    headers = {
        "User-Agent": "Mozilla/5.0"
    }



########################################################## 

# FULL PAGE

    for link in links:


        response = requests.get(link, headers=headers)
        
        soup = BeautifulSoup(response.text, "html.parser")

        jukugo_wrappers = soup.find_all("div", id=re.compile(r"^jukugo_\d+$"))

        for jukugo_wrapper in jukugo_wrappers:

            id_attr = jukugo_wrapper.get("id", "")

            match = re.search(r"jukugo_(\d+)", id_attr)
            id = match.group(1)



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
                result = kanji
            else: 
                result = kanji + " | " + furigana


            with open("vocab.txt", "a", encoding="utf-8") as f:
                f.write(result + "\t" + translations + "\n")



if __name__ == '__main__':

    scrape()