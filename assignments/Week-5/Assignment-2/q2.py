from typing import Dict


def countChar(s: str) -> Dict[str, int]:
    d = {}
    for c in s:
        if c in d:
            d[c] = d[c] + 1
        else:
            d[c] = 1
    return d


print(countChar("delhi delhi"))  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
