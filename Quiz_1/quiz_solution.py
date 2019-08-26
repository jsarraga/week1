

def readcurrency(filename):
        with open(filename, 'r') as file_obj:
                lines = file_obj.readlines()
                line_list = []
                line_dict = {}
                for line in lines:
                        line = line.split()
                        line_dict[line[0]] = line[1]
                        # line_dict['symbol'] = line[0]
                        # line_dict['rate'] = line[1]
                for key,value in line_dict.items():
                        line_list.append({key,value})

                        #need to name the keys and values to "symbol" and "rate"
        
        return line_list

print(readcurrency('currency.txt'))

def save(filename, data):
        with open(filename, 'w') as f_obj:
                f_obj.write(data)




