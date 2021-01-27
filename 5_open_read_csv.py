import csv


def write_csv(data):
    with open('name.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow((data['name'], data['surname'],data['age']))


def write_csv_order(data):
    with open('name.csv', 'a') as file:
        order = ['name','age','surname']
        writer = csv.DictWriter(file, fieldnames=order)
        writer.writerow(data)

def main():
    d = {'name':'Petr', 'surname':'Ivanov','age':21}
    d1 = {'name':'Ivan', 'surname':'Ivanov','age':18}
    d2 = {'name':'Ksu', 'surname':'Petrova','age':32}

    l = [d, d1, d2]

    # for i in l:
    #     write_csv_order(i)

    with open('cmc.csv') as file:
        field_names = ['1', '2', '3']
        reader = csv.DictReader(file, fieldnames=field_names)
        for row in reader:
            print(row)


if __name__ == '__main__':
    main()
