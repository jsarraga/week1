
def read_matrix(filename):
    """ loads a text file of a grid of integers and creates a list of lists
    of integers representing the matrix. matrix[r][c] is the element on
    row #r and column #c """
    with open(filename, 'r') as input_file:
        return ([[int(column) for column in row.split()] for row in input_file])


mylist  = read_matrix('testmatrix0.txt')

def m_print(alist):
    for i in alist:
        for j in i:
            print(j, end =" ")
        print()

m_print(mylist)

input()

def rowsum(alist):
    summed_list = [sum(i) for i in alist]
    return summed_list

#print(rowsum(mylist))
rowsumlist = rowsum(mylist)
print("Row Sums: ", *rowsumlist)

##alternate way
# def row_summer(dataset):
#     row_sums = []
#     for i in range(len(dataset)):
#         for j in dataset:
#             rowsums.append(sum(dataset[i]))
#             break

def colsum(alist):
    colsum =  list(map(sum, zip(*mylist)))
    return colsum

#print(colsum(mylist))
colsumlist = colsum(mylist)
print("Column Sums: ", *colsumlist)

#alternate way
# def column_summer(dataset):
#     column_sums = []
#     for i in range(len(dataset[0]))
#         sum = 0
#         for data_list in dataset:
#             sum += data_list[i]
#         column_sums.append(sum)

input()

row_summed = rowsum(mylist)
row_sort = sorted(row_summed)

def sorted_matrix1(asumlist, alist):
    dict1 = {}
    for summed, row in zip(asumlist, alist):
        dict1[summed] = [row]
    for key in sorted(dict1.keys()) :
        print(*dict1[key])

sorted_matrix1(row_summed, mylist)

input()

col_summed = colsum(mylist)
col_sort = sorted(col_summed)

def sorted_matrix2(asumlist, alist):
    dict2 = {}
    for summed, col in zip(asumlist, alist):
        dict2[summed] = [col]
    for key in sorted(dict2.keys()) :
        orint(*dict2[key])

print(sorted_matrix2(col_summed, mylist))