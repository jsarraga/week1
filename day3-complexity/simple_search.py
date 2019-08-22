our_list = [1, 2, 4, 7, 10, 14, 93, 100, 200, 1, 2, 4, 7, 10, 14, 93, 100, 200]

def simple_search(a_list, item):
    total = 0
    for i in a_list:
        for j in range(len(a_list)):
            for k in range(len(a_list)):
                for l in range(len(a_list)):
                    total += 1
    return False, total

print(simple_search(our_list, 9))