class Solution:
    def romanToInt(self, s: str) -> int:
        key={'I':1,'V':5,'X': 10,'L':50,'C':100,'D':500,'M':1000}
        answ=key[s[-1]]
        for i in range(len(s)-2,-1,-1):
            if key[s[i]] >= key[s[i + 1]]:
                answ+=key[s[i]]
            else:
                answ-=key[s[i]]
        return answ