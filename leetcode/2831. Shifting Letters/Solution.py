class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        pre = [0] * (n + 1)
    
        for start, end, move in shifts:
            pre[start] += 1 if move == 1 else -1
            pre[end + 1] += -1 if move == 1 else 1

        prefix = [0]
        for i in range(n):
            prefix.append(prefix[-1] + pre[i])

        result = ''
        for i in range(0, n):
            shift = prefix[i + 1] % 26
            result += chr( (ord(s[i]) - ord('a') + shift) % 26 + ord('a') )
        return result