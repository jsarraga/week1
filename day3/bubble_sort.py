

our_list = [4, 7, 2, 10, 14, 93, 100, 1] #how to sort this without a sort function
                                    #if i is greater than the number next to it, we'll flip them

def bubble_sort(a_list):
    
    n = len(a_list)
    total = 0

    for i in range(n):

        for j in range(0, n-i-1):

            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j] #basically x,y = y,x
            
            total += 1
            print("Total: {}, List: {}".format(total, a_list))
    return a_list, total

print(bubble_sort(our_list))

#conceptually: as the size of the list grows, the # of operations exponentially grow. NO BUENO


#big O operation -> O()
#looking up a key in a dictionary is one operation or O(1)
#a list takes n operations or O(n)



