
with open("outputfile.txt", "w") as file_object:
    file_object.write("first string\n")
    file_object.write("second string\n")
    file_object.write("third string\n")

with open("outputfile2.txt", "w") as file_object:     #writing to a file
    print("first string", file=file_object)
    print("second string", file=file_object)


with open("outputfile3.txt", "a") as file_object:  #appending to a file
    print("third line", file=file_object)


    #you can use write or print to write to a new file

"""
THIS CODE IS WRONG, IT'S A COMMON ERROR:

for line in source:
    with open("myfile.txt", "w") as file_object:
        file_object.write(line + '\n')

IF with open IS INSIDE OF A FOR LOOP, IT WILL
DELETE THE LAST STEP OF THE LOOP EACH TIME
"""
