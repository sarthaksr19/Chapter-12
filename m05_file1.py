def greet(name):
    print(f"good morning, {name}")
#  ''' this name method contain main parameter in it as we use above function in a diffrent file we don't want to add below statement so we use this main method it return false whenever we use this file fucntion in another file'''
if __name__ == "__main__":
    n = input("enter your name\n")
    greet(n)