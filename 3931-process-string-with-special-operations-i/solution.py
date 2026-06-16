class Solution:
    def processStr(self, s: str) -> str:
        result = ""
        for i in s:
            if (ord("a") <= ord(i) <= ord("z")) or (ord("A") <= ord(i) <= ord("Z")):
                result += i
            elif i == "*":
                result = result[:-1]
            elif i == "#":
                result = 2 * result
            elif i == "%":
                result = result[::-1]
        return result

