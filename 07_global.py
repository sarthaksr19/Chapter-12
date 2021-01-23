a = 11  # Global variable
def func1():
    global a
    print(a)  #prints global variable
    a = 19  # Local variable
    print(a)   #prints local variable

func1()
print(a)  #changes as global variable re-define in function defining. 11 ---> 19.