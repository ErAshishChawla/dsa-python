my_dict = {
    "Ashish": [1, 2, 3],
    "Sachin": [4, 5, 6],
    "Rahul": [7, 8, 9],
    "Virat": [10, 11, 12],
    "Rohit": [13, 14, 15],
}

for k, v in my_dict.items():
    total = 0
    for i in v:
        total += i
    print(f"{k} : {total} marks")
    print(f"{k} : {total/len(v)}%")
