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

    with open("translations.txt", "a", encoding="utf-8") as f:
        f.write("#separator: tab\n#html:true\n")


    headers = {
        "User-Agent": "Mozilla/5.0"
    }


    for link in links:


        response = requests.get(link, headers=headers)
        
        soup = BeautifulSoup(response.text, "html.parser")

        jukugo_wrappers = soup.find_all("div", id=re.compile(r"^jukugo_\d+$"))

        for jukugo_wrapper in jukugo_wrappers:


            vm_divs = jukugo_wrapper.find_all("div", class_="vm")

            translations= ', '.join(
                ''.join(child.strip() for child in div.contents if isinstance(child, NavigableString) and child.strip())
                for div in vm_divs
            )



            with open("translations.txt", "a", encoding="utf-8") as f:
                f.write(translations + "\n")



if __name__ == '__main__':

    scrape()