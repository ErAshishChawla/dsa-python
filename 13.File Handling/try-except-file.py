try:
    f = open("hello1.txt", "r")
    f.close()
except FileNotFoundError:
    print("File not found!")
except:
    print("Some error occurred!")
