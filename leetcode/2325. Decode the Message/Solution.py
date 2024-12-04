class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alphabet=list("abcdefghijklmnopqrstuvwxyz")
        keys=list(key)
        keylist=[]
        for elem in keys:
            if elem not in keylist and elem !=' ':
                keylist.append(elem)
        tuples=list(zip(keylist,alphabet))
        tuples.append((' ',' '))

        answer=[]
        for letter in message:
            for elem in tuples:
                if elem[0]==letter:
                    answer.append(elem[1])
                    break
        return(''.join(answer))