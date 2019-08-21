our_list = [1, 2, 0, 8, 6, 23]

def insertion_sort(a_list):
    n = len(a_list)
    total = 0

    for i in range(1, n):
        key = a_list[i]
        j = i - 1

        while j >= 0 and key > a_list[j]:
            a_list[j + 1] = a_list[j]
            j -= 1
            total += 1

        a_list[j + 1] = key
        print("Total: {}, List: {}".format(total, a_list))
        input()
    return a_list, total

print(insertion_sort(our_list))

#bubble sort compares element next to it, insertion sort compares it to the number larger or smaller to find the right spot for it
#conceptually: insertion takes fewer operations to sort. SLIGHTLY optimizes it