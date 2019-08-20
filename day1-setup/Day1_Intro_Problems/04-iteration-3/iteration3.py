mylist = [2, 34, 12, 29, 38, 1, 12, 8, 8, 9, 29, 38, 8, 9, 2, 3, 7, 10, 12, 8, 34, 7]

def medianl(alist):
    sorted_list = sorted(alist)
    len_list = len(sorted_list)
    if len_list < 1:
        return None
    if len_list % 2 == 0:
        index1 = (len_list - 1) // 2
        index2 = (len_list + 1) // 2
        med = (sorted_list[index1] + sorted_list[index2]) / 2
        print(med)
    else:
        index3 = (len_list)/ 2
        print(sorted_list[index3])
    

medianl(mylist)

def listavg(alist):
    avg = sum(alist)/len(alist)
    print(round(avg, 2))

listavg(mylist)

def numocc(alist):
    occ = 0
    num = alist[0]
    for i in alist:
        if alist.count(i) > occ:
            occ = alist.count(i)
            num = i 
            print(num)

numocc(mylist)


        
