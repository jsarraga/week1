import csv

with open('NHL_2018.csv', 'r') as f:
    reader = csv.DictReader(f)
    data = []
    for row in reader:
        sublist = []
        if row["Tm"] == 'DET':
            sublist.append(row)
            data.append(sublist)

with open ('output.csv', 'w') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)



# print(data)
 



with open('output.csv', 'r') as file_obj:
    