def maxFrequencyChar(string: str) -> str:
    freq = {}
    max_freq_char = ""
    max_freq = 0

    for chr in string:
        if chr in freq:
            freq[chr] += 1
        else:
            freq[chr] = 1

        if freq[chr] > max_freq:
            max_freq = freq[chr]
            max_freq_char = chr

    return max_freq_char


print(maxFrequencyChar("hellooooo world"))  # l
