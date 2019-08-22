def nuggs(x):
    if x == 0:
        return True
    if x < 0:
        return False
    
    return nuggs(x-6) or nuggs(x-9) or nuggs(x-20)

nugg_numbers = list(filter(nuggs,range(200)))


not_nugg = []
for i in range(200):
    if i in nugg_numbers:
        pass
    else:   
        not_nugg.append(i)

print("Not McNugget Numbers: ", not_nugg)


def nugg2015(x):
    if x == 0:
        return True
    if x < 0:
        return False

    return nugg2015(x-4) or nugg2015(x-6) or nugg2015(x-10) or nugg2015(x-20) or nugg2015(x-40)

nuggnum2015 = list(filter(nugg2015, range(200)))

print(nuggnum2015)