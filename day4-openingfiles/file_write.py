with open('outputfile.txt', 'w') as file_obj:     #writing to a file
    file_obj.write('first string\n')
    file_obj.write('second string\n')

with open('outputfile3.txt', 'a') as file_obj: #appending to a file
    print('This is a new line!!', file=file_obj')

#you can use write or print to write to a new file

