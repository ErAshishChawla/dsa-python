my_details = [
    {"name": "Anirudh", "age": 67, "gender": "Male"},
    {"name": "Clara", "age": 52, "gender": "Female"},
    {"name": "Vandana", "age": 63, "gender": "Female"},
    {"name": "Amber", "age": 23, "gender": "Male"},
]

print(my_details[1]["age"])
print(my_details[3]["gender"])

# Sort by age
sorted_details = sorted(
    my_details, key=lambda x: x["age"] if "age" in x else 9999999999
)
print(sorted_details)
