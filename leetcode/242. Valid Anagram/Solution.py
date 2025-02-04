class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        setS = set(s)
        setT = set(t)

        if setS != setT:
            return False
        
        for letter in setS:
            if s.count(letter) != t.count(letter):
                return False
        
        return True