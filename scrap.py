import requests
from bs4 import BeautifulSoup as bs
import re


def scrapit(url):
    res = requests.get(f'https://en.wikipedia.org/wiki/{url}')
    soup = bs(res.text, 'lxml')

    allowed = 'ph1h2h3h4' #tags to scrap
    first_heading = soup.find('h1')
    element = first_heading
    alldata = []
    while(True):
        # stop scrapping at See also
        if "See also" in element.text or "References" in  element.text:
            break
        # remove all [Edit] and [ref]
        data = re.sub(re.compile(r'\[\w+\]'), '',   element.text)
        alldata.append(f'[{element.name}] {data}')
        element = element.findNext()
        while(True):
            if element.name not in allowed or element.text == "Contents": #skip contents heading
                element = element.findNext()
                continue
            break
    return alldata
