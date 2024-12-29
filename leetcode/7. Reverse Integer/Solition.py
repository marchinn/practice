class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        num=str(x)
        
        if num[0]=="-":
            flag=-1
            reverse_x = num[1:][::-1]
        else:
            flag=1
            reverse_x = num[::-1]
        
        res = 0
        i = len(reverse_x)-1
        for digit in reverse_x:
            res += int(digit)*(10**i)
            i -= 1
        
        res=res*flag
        if res >= -(2)**31 and res <= (2)**31-1:
            return res
        else:
            return 0