import sys

input_file = input("Enter file to copy from: ")
output_file = input("Enter file to copy to: ")

try:
    f = open(input_file, "r")
    data = f.read()
    f.close()
except FileNotFoundError:
    print("File not found")
    sys.exit()
except:
    print("Something went wrong")
    sys.exit()

try:
    f = open(output_file, "w")
    f.write(data)
    f.close()
except:
    print("Something went wrong")
    sys.exit()
