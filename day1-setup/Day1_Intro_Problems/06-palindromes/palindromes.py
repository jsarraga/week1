def is_palindrome(astring):
    rev = astring[::-1]
    if astring == rev:
        print(True)
    else:
        print(False)


is_palindrome("tacocat")
