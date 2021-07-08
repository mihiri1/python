num = int(input("Enter Your Marks: "))

if 100 >= num >= 0:
    if num >= 75:
        print("A")
    elif num >= 50:
        print("B")
    elif num >= 35:
        print("C")
    else:
        print("FAIL")


else:
    print("Invalid MARKS")
