import requests
from bs4 import BeautifulSoup
import csv


URL = 'https://coinmarketcap.com/'

def get_html(url):
    r = requests.get(url)
    # print(r.content)
    return r.text


def get_data(data):
    soup = BeautifulSoup(data, 'lxml')
    i = 0
    while i<100:
        try:
            tds = soup.find('tbody').find_all('tr')[i]
            for td in tds:
                print(td.text)
                # print(type(td))
                # print(len(td))
        except:
            print('except')
        i +=1

def main():
    get_data(get_html(URL))


if __name__ == '__main__':
    main()
