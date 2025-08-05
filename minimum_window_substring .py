from collections import Counter

def min_window(s, t):
    if not t or not s:
        return ""

    dict_t = Counter(t)
    window_counts = {}
    required = len(dict_t)
    l = r = formed = 0
    min_len = float('inf')
    ans = (0, 0)

    while r < len(s):
        character = s[r]
        window_counts[character] = window_counts.get(character, 0) + 1

        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1

        while l <= r and formed == required:
            if r - l + 1 < min_len:
                min_len = r - l + 1
                ans = (l, r)
            
            window_counts[s[l]] -= 1
            if s[l] in dict_t and window_counts[s[l]] < dict_t[s[l]]:
                formed -= 1
            l += 1
        r += 1

    return s[ans[0]:ans[1]+1] if min_len != float('inf') else ""
