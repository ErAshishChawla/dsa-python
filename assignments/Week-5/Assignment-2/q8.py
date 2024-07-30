my_dict = {
    "Ashish": [11, 2, 3],
    "Sachin": [4, 5, 6],
    "Rahul": [7, 8, 9],
    "Virat": [10, 11, 12],
    "Rohit": [1, 14, 15],
}


def cSort(l: list[int]) -> list[int]:
    sorted_list = l.copy()
    for i in range(len(sorted_list) - 1):
        for j in range(i + 1, len(sorted_list)):
            if l[i] > l[j]:
                temp = l[i]
                l[i] = l[j]
                l[j] = temp
    return l


total_marks = []


for k, v in my_dict.items():
    total = 0
    for i in v:
        total += i
    total_marks.append(total)

temp_list = total_marks.copy()

print(total_marks)
print(cSort(temp_list))
