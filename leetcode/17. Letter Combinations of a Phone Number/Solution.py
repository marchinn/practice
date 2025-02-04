import itertools

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        key={
            '1': [],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
            }
            
        if not digits:
            return []
        
        letters=[]
        for digit in digits:
            if digit in key:
                letters.append(key[digit])
        
        combs = list(itertools.product(*letters))
        return [''.join(comb) for comb in combs]