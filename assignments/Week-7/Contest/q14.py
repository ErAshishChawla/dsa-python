def mergeFiles(file1, file2):
    with open(file1, "r") as f1:
        data1 = f1.readlines()
    with open(file2, "r") as f2:
        data2 = f2.readlines()

    modified_data1 = [i.strip() for i in data1]
    modified_data2 = [i.strip() for i in data2]

    combined_data = modified_data1 + modified_data2

    with open("output.txt", "w") as f3:
        f3.write("\n".join(combined_data))


mergeFiles("test.txt", "test2.txt")
