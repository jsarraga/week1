import json

# def req_to_json(filename):
with open('requirements.txt', 'r') as f:
    pair_list = []
    pair_dict = {}
    for line in f:
        list_line = line.strip("\n")
        lines = list_line.split("==")
        pair_list.append(lines)

    list_length = len(pair_list) - 1
    for i in pair_list[0:list_length]:
        pair_dict[i[0]] = i[1]

with open('requirements.json', 'w') as json_file:
    json.dump(pair_dict, json_file, indent=2)


