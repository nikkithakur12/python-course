a = int(input("Enter a number"))
b = int(input("Enter a second number"))

if (b == 0 ):
    raise ZeroDivisionError("Hey our programm is not meant to devided by zero")
else:
    print(f"the division a/b is{a/b}")