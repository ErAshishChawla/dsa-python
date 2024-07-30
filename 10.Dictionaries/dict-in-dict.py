students = {
    "anirudh": {
        "age": 66,
        "gender": "Male",
    },
    "sanjay": {
        # "age": 11,
        "gender": "Male",
    },
    "vandana": {
        "age": 53,
        "gender": "Female",
    },
}


for k,v in students.items():
    print(f"{k} has age = {v["age"] if "age" in v else 'N/A'}")
