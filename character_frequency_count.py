def most_frequent_char(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    max_char = max(freq, key=freq.get)
    return max_char, freq[max_char]

print(most_frequent_char("hello"))  # ('l', 2)
