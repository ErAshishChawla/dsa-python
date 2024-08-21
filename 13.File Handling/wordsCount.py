f = open("hello.txt", "r")

# d = f.read()
# print(len(d.split()))

# lines = f.readlines()
# for line in lines:
#     print(len(line.split()))

lines = f.readlines()
for line in lines:
    print(" ".join(line.split()[::-1]))

f.close()
