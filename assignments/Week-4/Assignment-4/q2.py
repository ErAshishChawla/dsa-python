def words(s: str) -> list[str]:
    word_list = []

    start = 0
    end = 1

    l = len(s)

    while True:
        if end == l:
            if s[start] == " ":
                break
            else:
                word_list.append(s[start:])
                break
        elif start >= l:
            break
        if s[end] == " ":
            if s[start] == " ":
                start = start + 1
                end = end + 1
            else:
                word_list.append(s[start:end])
                start = end + 1
                end = start + 1
        elif s[end] != " ":
            if s[start] == " ":
                start = start + 1
                end = end + 1
            else:
                end += 1
    return word_list
    # return s.split()


print(words("pyt  hon is  great     .  .          "))
