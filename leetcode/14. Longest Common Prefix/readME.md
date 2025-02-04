# [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix)

####
```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        min_length = min(len(s) for s in strs)
        prefix = ''

        for i in range(min_length):
           
            for s in strs:
                if s[i] != strs[0][i]:
                    return prefix
            
            prefix += strs[0][i]
        
        return prefix
```