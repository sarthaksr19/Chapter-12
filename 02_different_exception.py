try:
    a = int(input("enter the number\n"))
    b = 1/a
    print(b)

except ValueError as e:   # catching the valueerror occurence
    print("enter the valid divisible value ")

except ZeroDivisionError as e:    # catching the zerodivisionerror occurence
    print("make sure you are not dividing by 0")
