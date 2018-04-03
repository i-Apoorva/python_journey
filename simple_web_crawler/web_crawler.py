import requests
from bs4 import BeautifulSoup


def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'http://codecanyon.net/search?date=&page=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for link in soup.findAll('a'):
            href = 'http://codecanyon.net' + link.get('href')
            # print(href)
            # print(title)
            get_single_item_data(href)
        page += 1


def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text

    soup = BeautifulSoup(plain_text, "html.parser")
    for item_name in soup.find_all('div'):
        print(item_name)


trade_spider(6)