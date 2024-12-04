import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        match=re.fullmatch(p,s) 
        return (True if match else False)