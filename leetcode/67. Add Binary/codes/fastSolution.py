class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        num=bin(int(a, 2) + int(b, 2))
        return num[2:]