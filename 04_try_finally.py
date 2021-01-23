try:
    a = int(input("Enter the number "))
    b = 1/a
    print(b)

except Exception as e:
    print(e)
    exit()

finally:
    print("this block of code is exceuted whatever happens in programme whether you exit the program earlier or not.")