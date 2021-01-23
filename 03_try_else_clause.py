try:
    a = int(input("enter the number "))
    b = 1/a
    print(b)

except Exception as e:
    print(e)

else:
    print("this else block only exceutes when try method is true otherwise it dosen't")