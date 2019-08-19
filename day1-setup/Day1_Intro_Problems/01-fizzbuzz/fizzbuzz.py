#!/usr/bin/env/python3
def fizz(x):
    loop = range(x)
    for i in loop:
        if i == 0:
            continue
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print ("Buzz")
        else:
            print(i)

print(fizz (20))
