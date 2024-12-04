# [509. Fibonacci Number](https://leetcode.com/problems/fibonacci-number)

####
```python
class Solution:
    def fib(self, n: int) -> int:
        match n:
            case 0:
                return 0
            case 1:
                return 1
            case _:
                nums=[0,1]
                n1,n2=1,0
                for k in range(2,n):
                    nums.append(n1+n2)
                    n2,n1=n1,n1+n2
                return (nums[-1]+nums[-2])
```