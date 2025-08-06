def replace_vowels(s):
    vowels = 'aeiouAEIOU'
    result = ""
    for char in s:
        if char in vowels:
            result += '*'
        else:
            result += char
    return result

print(replace_vowels("Hello World"))
