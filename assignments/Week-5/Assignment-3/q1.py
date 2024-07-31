d = {
    1: 2,
    3: 4,
    4: 3,
    2: 1,
    0: 0,
}

asc_sorted = dict(sorted(d.items(), key=lambda x: x[1]))
desc_sorted = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

print(f"Asceding: {asc_sorted}")
print(f"Descending: {desc_sorted}")
