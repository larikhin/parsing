import requests
from bs4 import BeautifulSoup
import requests_info_status_code
import csv


url = 'https://zakupki.gov.ru/epz/order/extendedsearch/results.html'

def write_csv(data):
    if data['price'] <= 500000: # filter by volume of price
        with open('tenders.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow((data['number'],
                            data['title'],
                            data['value'],
                            # data['client_link'], # need not this information
                            data['price']))
            print('add in csv')


def get_html(url):
    print('___________asking from server information_____________')
    r = requests.get(url)   # asking from server information
    requests_info_status_code.print_info(r.status_code)
    print('________________return information____________________')
    return r.text           # text give the html datas


def get_datas(html):
        #scaning datas
    print('___________scaning datas by BeautifulSoup_____________')
    soup = BeautifulSoup(html, 'lxml')
    print('____________filtering the datas_______________________')
    find_result = soup.body
    find_result = find_result.form
    find_result = find_result.find_all('div', class_= 'row no-gutters registry-entry__form mr-0')
    print('_______start collecting filter result_________________')
    for i in find_result:
            # it is number or order(tender)
        number = i.find('div', class_= 'registry-entry__header-mid__number')
        number = number.text.strip()

            # it is status of tender
        title = i.find('div', class_= 'registry-entry__header-mid__title')
        title = title.text.strip()

            # it is description on tender
        value = i.find('div', class_= 'registry-entry__body-value')
        value = value.text.strip()

            # it is name of client
        client_link = i.find('div', class_= 'registry-entry__body-href')
        client_link = client_link.a.text.strip()

            # it is start price
        price = i.find('div', class_= 'price-block__value')
        price = price.text.strip()
        price = price.replace("\xa0", "")
        price = price.replace(" ₽", "")
        price = price[:-3]
        price = int(price)
            # add collected data to dict
        data ={'number': number,
                'title': title,
                'value': value,
                'client_link': client_link,
                'price': price}

            # call function to write data in csv
        write_csv(data)

        print('next one')
    print('_______finish collecting and writing data_________________')

def main():
    get_datas(get_html(url))

if __name__ == '__main__':
    main()
