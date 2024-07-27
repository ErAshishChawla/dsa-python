my_string = "python is great"

result = my_string.split("on")
print(result)

result = my_string.split()
reveresed_result = result[::-1]
print(" ".join(i for i in reveresed_result))

input_string: str = input("Enter a string: ")
print("Input string ->", input_string)
result: list[str] = input_string.split()
reversed_result: list[str] = result[::-1]
print(" ".join(i for i in reversed_result))
