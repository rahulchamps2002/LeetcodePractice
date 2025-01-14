# Longest Substring Without Repeating Characters
### Difficulty: <font color=orange>Medium</font>
## Question Description: 

Given a string **_`s`_** find the length f the **longest substring** without repeating characters.

```angular2html
Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3
```
```angular2html
Example 2: 
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.
```
```angular2html
Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

## <font color=green>Solution:</font>
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        letters = set()
        
        for i in range(len(s)):
            while s[i] in letters:
                letters.remove(s[l])
                l += 1
            letters.add(s[i])
            res = max(res, i - l + 1)
        return res
```

## Explanation of Solution:
`l = 0` represents the number of letters we removed from the set
`res = 0` is the initialization of the result variable and is initialized with zero. Zero is our base case.
`letters = set()` is the set we we will use to keep track of our longest substring
