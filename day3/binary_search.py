our_list = [4, 7, 2, 10, 14, 93, 100]

def binary_search(a_list, l, r, x):   #left(l) is first element, right(r) is endpoint, x is what we're looking for
                                    #if x is in the left half of the list, we'll move r to the middle (or vice versa) until we find x
    total = 0

    while l <= r:
        total += 1
        mid = round(l + (r-l)/2)

        if a_list[mid] == x:
            return mid, total
        elif a_list[mid] < x:
            l = mid + 1
        else:
            r = mid -1
    return False, total

result = binary_search(our_list, 0, len(our_list)-1, 100)
print(result)