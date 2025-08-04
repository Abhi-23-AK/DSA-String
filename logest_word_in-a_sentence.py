def longest_word(sentence):
    words = sentence.split()
    max_word = max(words, key=len)
    return max_word

print(longest_word("I am learning data structures"))  # "structures"
