class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        n = len(strs)
        if len(strs) == 1:
            return strs[0]

        for i in range(len(strs[0])):
            for j in range(1,n):
                if i>=len(strs[j]):
                    break
                if strs[0][i] == strs[j][i]:
                    if j == n-1:
                        result += strs[0][i]
                else:
                    return result
        return result
        
            
                 
