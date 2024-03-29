import csv


with open('airtravel.csv', 'r') as file_object:
    reader = csv.reader(file_object)
    for row in reader:
        print(row)

with open('hurricanes.csv', 'r') as file_object: ##dict reader to access data by keys, values. assumes first row is header and column header act as keys.
    reader = csv.DictReader(file_object)
    for row in reader:
        print(row['Month'])
        for key, value in row.items():
            print(key,value)

