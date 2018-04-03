import requests
from bs4 import BeautifulSoup

def trade_spider(max_page):
    page = 1
    while page <= max_page:
        url = 'https://www.etsy.com/c/accessories?order=most_relevant&use_mmx=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for link in soup.findAll('a'):
            href = link.get('href')
            print(href)
        page +=1

trade_spider(5)
