import requests
import csv
from bs4 import BeautifulSoup


# URL = 'https://yacca.ru/cat/Entertainment/'

def refine_cy(strg):
    # ТИЦ: 4000 - ['ТИЦ', '4000']
    return strg.split(' ')[-1]

def get_html(url):
    r = requests.get(url)
    if r.ok:
        return r.text
    print(r.status_code)


def write_csv(data):
    with open('yaca.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'],
                                data['url'],
                                data['snipet'],
                                data['cy']))


def get_data_html(html):
    soup = BeautifulSoup(html, 'lxml')
    lis = soup.find_all('li', class_='yaca-snippet')

    for li in lis:
        try:
            name = li.find('h2').text
        except:
            name = ''

        try:
            url = li.find('h2').find('a').get('href')
        except:
            url = ''

        try:
            snipet = li.find('div', class_='yaca-snippet__text').text.strip()
        except:
            snipet = ''

        try:
            cy = li.find('div', class_='yaca-snippet__cy').text.strip()
            cy = refine_cy(cy)
        except:
            cy = ''

        data = {'name':name,
        'url':url,
        'snipet':snipet,
        'cy':cy}

        write_csv(data)


def main():
    pattern = 'https://yacca.ru/cat/Entertainment/{}.html'
    for i in range(1, 50):
        url = pattern.format(str(i))
        get_data_html(get_html(url))
    pass


if __name__ == '__main__':
    main()
