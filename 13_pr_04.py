try:
    a = int(input("enter the divider integer number\n"))
    b = int(input("enter the divisible integer number\n"))
    c = a/b
    print(c)

except ZeroDivisionError as e:
    print("infinite!!")

