with open("test.txt", "r") as f:
    all_text = f.read()

no_of_characters = len(all_text)
no_of_words = len(all_text.split())

with open("test.txt", "r") as f:
    all_lines = f.readlines()

no_of_lines = len(all_lines)
print(f"Characters: {no_of_characters}\nWords: {no_of_words}\nLines: {no_of_lines}")
