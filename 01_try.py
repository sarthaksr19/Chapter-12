while(True):
    print("press q to quit")
    a = input("Enter the number\n")
    if a == 'q':
        break
    try:
        a = int(a)
        if a>10:
            print("you entered a number greater than 10")
    except Exception as e:
        print(f"your input result throws an error: {e}")

print("Thanks for playing this game")