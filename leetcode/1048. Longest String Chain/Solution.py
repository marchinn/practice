class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        lengthOfWords={}
        maxLen=1

        def isPredecessor(wordB: str, wordA: str) -> bool:
            if len(wordA) != len(wordB) + 1:
                return False
            for i in range(len(wordA)):
                if wordA[:i] + wordA[i+1:] == wordB:
                    return True
            return False

        for i in range(len(words)):
            lengthOfWords[words[i]]=1
            for j in range(i):
                if isPredecessor(words[j], words[i]):
                    lengthOfWords[words[i]] = max(lengthOfWords[words[i]], lengthOfWords[words[j]]+1)
                    maxLen = max(maxLen, lengthOfWords[words[i]])
        return maxLen