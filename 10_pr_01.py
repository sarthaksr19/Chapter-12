def readFile(filename):
    try:
        with open(filename,"r") as f:
            print(f.read())
    
    except FileNotFoundError as e:
        print(f"Error! {filename} file is not found")

readFile("1.txt")
readFile("2.txt")
readFile("3.txt")
