# ______________________________________________________________________________
from bs4 import BeautifulSoup
import re # regular expressions

# .find() - only one and Tag
# .find_all() - all founded and ResultSet
# .parent
# .find_parent()
# .parents
# .find_parents()

# .find_next_sibling()
# .find_previous_sibling() brother

# filter by 're' regular expressions
re.compile('\d{1,100}')
# ^ начало строки
# $ конец строки
# . любой символ
# + неограниченное количество вхождений
# '\d' цифра
# '\w' буквы, цифры

def salary(soup):
    salary = soup.find_all('div', {'data-set':'salary'})
    for s in salary:
        print(s.text)
        get_what(s.text)


        # pythex.org validation regular expressions
def get_what(where):
    what = r'\d{1,9}' #pythex.org for more regular expressions
    salary_1 = re.search(what, where).group()
    salary_2 = re.findall(what, where)[0]
    print(salary_1, salary_2)

# Tag filter function
def copy_writer(tag):
    who_is = tag.find('div', id='whois').text.strip()
    if 'Copywriter' in who_is:
        return tag
    return None


def cw(soup):
    copywriters = []
    rows = soup.find_all('div', class_='row')
    for item in rows:
        a = copy_writer(item)
        if a:
            copywriters.append(a)
        print(copywriters)

# filter by filter_by_commands
def filter_by_commands(soup):
    # filtering and  checking
    row_1 = soup.find('div', class_='row')
    row_2= soup.find('div', {'class':'row'})
    # equal methods - True
    print(row_1==row_2)
    # only one working methods ! {'x': 'y'}
    data_set_Tag = soup.find('div', {'data-set':'salary'})
    data_set_RS = soup.find_all('div', {'data-set':'salary'})
    print(type(data_set_Tag),type(data_set_RS))
    # filter parent
    alena = soup.find('div', text='Alena')
    alena_parent = alena.parent
    print(alena_parent)
    # find_next_sibling
    container_alena = soup.find('div', {'class':'container'}).find('div', text='salary: 2100 usd')
    c_a_previous = container_alena.find_previous_sibling()
    c_a_next = container_alena.find_next_sibling()
    print(c_a_previous,container_alena, c_a_next)



def main():
        # open and reading
    file = open('index.html').read()
        # scaning from file by soup
    soup = BeautifulSoup(file, 'lxml')
        # filter by filter_by_commands
    # filter_by_commands(soup)
        # filter by script
    # cw(soup)
        # filter by script
    salary(soup)


if __name__ == '__main__':
    main()
