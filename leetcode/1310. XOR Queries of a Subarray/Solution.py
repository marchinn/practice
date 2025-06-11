class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0]
        for num in arr:
            prefix.append(num ^ prefix[-1])

        answer = []
        for left, right in queries:
            res = prefix[right + 1] ^ prefix[left]
            answer.append(res)

        return answer