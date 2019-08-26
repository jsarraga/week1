import json

# * Write a function ```readcurrency(filename)```

def readcurrency(filename):
    # read the lines of a file
    with open(filename, 'r') as file_object:
        lines = file_object.readlines()
        new_list = []
    # Separate lines into two values
        for line in lines:
            new_dict = {}
            line = line.strip().split()
            new_dict['symbol'] = line[0]
            new_dict['rate'] = float(line[1])
            new_list.append(new_dict)
    return new_list

# print(readcurrency('currency.txt'))

def save(filename, a_list):
    with open(filename, 'w') as file_object:
        new_data = {'data': a_list}
        json.dump(new_data, file_object, indent=2)


save('currency.json',readcurrency('currency.txt'))