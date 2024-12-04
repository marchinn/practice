import itertools
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        perm=list(permutations(digits,3))
        nums=list(Counter(perm))
        arr=[]
        for el in nums:
            num=int(f"{el[0]}{el[1]}{el[2]}")
            if num>=100 and num%2==0:
                arr.append(num)
        return sorted(arr)