mylist = [1, 2, ['jeff', 'tom'], [42, ['billy', 'jason']]]

def i(alist):
    for i in alist:
        if type(i)== list:
            for l in i:
                if type(l) == list:
                    for a in l:
                        print(a)   
                else:
                    print(l)
        else:
            print(i)    

i(mylist)
