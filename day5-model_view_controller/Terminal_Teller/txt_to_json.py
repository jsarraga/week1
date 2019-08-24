#!/usr/bin/env python3

with open("requirements.txt") as t:
    # print(t.readlines())
    data = []
    dict_data ={}
    for line in t:
        # print(line, end='')
        list_line = line.strip('\n')
        lines = list_line.split("==")
        data.append(lines)
    datalength = len(data) - 1
    for element in data[0:datalength]:
        dict_data[element[0]] = element[1] 
    print (dict_data)
    