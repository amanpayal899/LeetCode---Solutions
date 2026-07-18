class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        t = ""
        xString = ""
        n = len(s)
        for i in range(n):
            if s[i] == x:
                xString += x
            else:
                t += s[i]
        t = t+xString
        return t
