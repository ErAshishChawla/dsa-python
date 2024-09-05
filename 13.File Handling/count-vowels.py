def countVowels(file_name: str) -> int:
    try:
        f = open(file_name, "r")
        data = f.read()
        f.close()

        vowels = "aeiou"
        count = 0
        for char in data:
            if char.lower() in vowels:
                count += 1
        return count
    except FileNotFoundError:
        print("File not found")
        return -1
    except:
        print("Something went wrong")
        return -1


print(countVowels("test.txt"))
