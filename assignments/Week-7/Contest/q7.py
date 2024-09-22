string = "Hello, World!"

try:
    i_index = int(input())
except ValueError:
    print("Invalid input")
    exit()
except:
    print("An error occurred")
    exit()

if i_index < 0 or i_index >= len(string):
    print("Invalid index")
    exit()

# Remove the character at the given index using slicing
new_string = string[:i_index] + string[i_index + 1 :]
print(new_string)

# Remove the character at the given index using a loop
new_string = ""
for i in range(len(string)):
    if i != i_index:
        new_string += string[i]
print(new_string)

# Remove i_index character from string using list comprehension
new_string = "".join([string[i] for i in range(len(string)) if i != i_index])
print(new_string)
