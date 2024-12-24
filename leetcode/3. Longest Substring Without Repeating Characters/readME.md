# [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters)

####
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if s=='':
            return 0

        symbols = set()
        lengths = []

        a = 0
        for b in range(len(s)):
            while s[b] in symbols:
                symbols.remove(s[a])
                a += 1
            symbols.add(s[b])
            lengths.append(b-a+1)

        return max(lengths)
```