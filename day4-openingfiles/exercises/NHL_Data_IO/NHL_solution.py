import csv

with open('NHL_2018.csv', 'r') as f:
    reader = csv.DictReader(f)
    data = []
    for row in reader:
        if row["Tm"] == 'DET':
            data.append(row)

with open('output.csv', 'w') as file_obj:
    writer = csv.writer(file_obj)
    for row in data:
        writer.writerow(row)



# print(data)
 