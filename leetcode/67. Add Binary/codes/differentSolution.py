class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0

        while len(a) > 0 or len(b) > 0 or carry:
            bitA = a[-1] if len(a) > 0 else 0
            bitB = b[-1] if len(b) > 0 else 0

            theirSum = int(bitA) + int(bitB) + carry
            carry = 1 if theirSum > 1 else 0

            if theirSum == 3:
                res += "1"
            elif theirSum == 2:
                res += "0"
            else:
                res += str(theirSum)

            a = a[:-1] if a else ""
            b = b[:-1] if b else ""

        return res[::-1]