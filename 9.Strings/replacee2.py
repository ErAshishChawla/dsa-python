my_string: str = "delhi is a clean city"

lst = list(my_string)
print(lst)

print("".join([ch if ch != "i" else "z" for ch in lst]))
