# [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring)

####
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''

        def check_match(s,i,j):
            while i>=0 and j<len(s):
                if s[i]!=s[j]:
                    break
                else:
                    i-=1
                    j+=1
            return i+1,j-1
        
        def check_len(indexes,i1,i2):
            if i2-i1>=indexes[1]-indexes[0]:
                indexes[1],indexes[0]=i2,i1
            return indexes
        
        indexes=[0,0]

        for i in range(len(s)):
            a,b=check_match(s,i,i)
            indexes=check_len(indexes,a,b)
            if i+1<len(s) and s[i]==s[i+1]:
                c,d=check_match(s,i,i+1)
                indexes=check_len(indexes,c,d)
        return s[indexes[0]:indexes[1]+1]
```