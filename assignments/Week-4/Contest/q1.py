def isPalindrome(s: str) -> bool:
    return s.lower() == s[::-1].lower()


print(isPalindrome("moom"))
print(isPalindrome("ABCcba"))
print(isPalindrome("ABCcbaa"))
