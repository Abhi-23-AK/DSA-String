def compress(chars):
    i = 0
    while i < len(chars):
        char = chars[i]
        count = 1
        while i + 1 < len(chars) and chars[i + 1] == char:
            count += 1
            chars.pop(i + 1)
        if count > 1:
            for c in str(count):
                chars.insert(i + 1, c)
                i += 1
        i += 1
    return len(chars)
