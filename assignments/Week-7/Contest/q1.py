def check_palindrome_1(s: str) -> bool:
    reversed_str = s[::-1]
    return s == reversed_str


def check_palindrome_2(s: str) -> bool:
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True


print(check_palindrome_1("racecar"))
print(check_palindrome_2("racecar"))
