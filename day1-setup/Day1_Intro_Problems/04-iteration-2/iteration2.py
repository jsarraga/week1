def my_loop(x):
    loop = range(x)
    for i in loop:
        print(i)

my_loop(10)

def my_reverse_loop(x):
    loop = range(x+1)
    print(loop)
    r = loop[::-1]
    for i in r:
        print(i)

my_reverse_loop(5)