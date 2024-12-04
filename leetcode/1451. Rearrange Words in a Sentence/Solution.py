import collections
class Solution:
    def arrangeWords(self, text: str) -> str:
        words=text.split(' ')
        words=[w.lower() for w in words]
        print(words)
        len_info=sorted(list(Counter(len(word) for word in words)))
        result=''
        for val in len_info:
            for word in words:
                if len(word)==val:
                    result+=str(word+' ')
        return result[0].upper()+result[1:-1]