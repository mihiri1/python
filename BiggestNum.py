x =int(input("Enter Num1: "))
y =int(input("Enter Num1: "))
z =int(input("Enter Num1: "))

if (x>y) and (x>z):
    largest_Number = x
elif (y>x) and (y>z):
    largest_Number = y
else:
    largest_Number = z

print("The Biggest Num is:", largest_Number)
