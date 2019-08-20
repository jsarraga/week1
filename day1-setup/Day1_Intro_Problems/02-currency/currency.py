

def currency_converter(amount):
    amount = float(amount)
    amount = amount * 100
    hundreds = amount // 10000
    amount = amount % 10000
    fifties = amount // 5000
    amount = amount % 5000
    twenties = amount // 2000
    amount = amount % 2000
    tens = amount // 1000
    amount = amount % 1000
    fives = amount // 500
    amount = amount % 500
    ones = amount // 100
    amount = amount % 100
    quarters = amount // 25
    amount = amount % 25
    dimes = amount // 10
    amount = amount % 10
    nickels = amount // 5
    amount = amount % 5
    pennies = amount // 1
    print(hundreds, " hundreds")
    print(fifties, " fifties")
    print(twenties, "twenties")
    print(tens, "tens")
    print(fives, " fives")
    print(ones, " ones")
    print(quarters, " quarters")
    print(dimes, " dimes")
    print(nickels, " nickels")
    print(pennies, " pennies")
    

currency_converter(input("How much are you converting? " ))