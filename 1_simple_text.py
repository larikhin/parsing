import requests                 # install lib from pip3
from bs4 import BeautifulSoup   # install lib from pip3, and install 'lxml' too!


url = 'https://wordpress.org/'

def get_html(url):
    r = requests.get(url)   # asking from server information
                            # type(r) Response
                            # dir(r) list of methods atributs
                            # if print(r.status_code)
                            # 200 all is ok!
                            # 403  acess denied
                            # 404, 404, 503 some errors
    # print(r.status_code)   # for test
    return r.text           # text give the html datas

def get_data(html): # use the data from html to soup
    # transforming data from html to python data tree
    # 'lxml' it is type of parser, we install lxml in pip3
    soup = BeautifulSoup(html, 'lxml')
    # what to find?
    h1 = soup.find('div', id='home-welcome').find('header').find('p').text
    #h2 = soup.p.text
    return h1

def main():
    # set the url for parsing
    # wrap the methods
    print(get_data(get_html(url)))


if __name__ == '__main__':
    main()
