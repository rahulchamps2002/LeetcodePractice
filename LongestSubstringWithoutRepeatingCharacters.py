def lengthOfLongestSubstring(s: str) -> int:
    l = 0
    res = 0
    letters = set()
    for n in range(len(s)):
        while s[n] in letters:
            letters.remove(s[l])
            l += 1
        letters.add(s[n])
        res = max(res, n - l + 1)
    return res

print(lengthOfLongestSubstring('pwwkew'))
