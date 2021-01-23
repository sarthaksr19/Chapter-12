num = int(input("enter the table number\n"))
t = [num*i for i in range(1,11)]  # by list comprehension
print(t)

with open("table.txt","a") as f:  #storing the table in a file.
    f.write(str(t))
    f.write("\n")