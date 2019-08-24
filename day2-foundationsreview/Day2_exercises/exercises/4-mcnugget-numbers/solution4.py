# def nuggs(x):
#     if x == 0:
#         return True
#     if x < 0:
#         return False
    
#     return nuggs(x-6) or nuggs(x-9) or nuggs(x-20)

# nugg_numbers = list(filter(nuggs,range(200)))

known = [0]
i = 1
consecutive_success = 0

while True:
    if i - 6 in known or i - 9 in known or i - 20 in known:
        known.append(i)
        consecutive_success += 1
        if consecutive_success == 6:
            print("All numbers >= {} are mcnugget".format(i-5))
            break
    else:
        print(i)
        consecutive_success = 0
    i += 1
    