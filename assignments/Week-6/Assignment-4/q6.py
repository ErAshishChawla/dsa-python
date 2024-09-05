def countVowels(src: str, dest: str) -> int | None:
    try:
        f = open(src, "r")
        data = f.readlines()
        f.close()

    except FileNotFoundError:
        print("File not found")
        return -1
    except:
        print("Something went wrong")
        return -1

    formatted_data = [line.strip() for line in data]

    try:
        f = open(dest, "w")
        for line in formatted_data:
            vowels = 0
            for char in line:
                if char in "aeiouAEIOU":
                    vowels += 1
            f.write(f"{line} {vowels}\n")
        f.close()
    except:
        print("Something went wrong")
        return -1


countVowels("test-q6.txt", "result-q6.txt")
