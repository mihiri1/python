num = int(input("Enter Num:"))

if (num % 2) == 0:
    print("{} is Even Number.".format(num))
else:
    print("{} is Odd Number.".format(num))

#OR

printString = "{} is {} Number."

if (num % 2) == 0:
    print(printString.format(num, "Even"))
else:
    print(printString.format(num, "Odd"))