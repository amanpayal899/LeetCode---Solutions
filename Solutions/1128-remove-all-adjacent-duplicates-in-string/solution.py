class Solution:
    def removeDuplicates(self, s: str) -> str:
        n = len(s)
        stack = []
        
        #🤦‍♂️ sometimes it feels so  easy!!
        for i in  range(n):
            if len(stack)==0:
                stack.append(s[i])
            elif s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
        result = ""
        for i in stack:
            result += i
        return result
