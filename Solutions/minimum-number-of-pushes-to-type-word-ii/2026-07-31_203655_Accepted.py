# Problem: Minimum Number of Pushes to Type Word II
# Status: Accepted
# Language: python3
# Runtime: 147 ms
# Memory: 20 MB
# Submitted: 2026-07-31_203655 UTC
# URL: https://leetcode.com/submissions/detail/2089284093/

class Solution:
    def minimumPushes(self, word: str) -> int:
        arr = [0]*26
        pushes = 0
        for ch in word:
            arr[ord(ch)-97] += 1
        
        arr.sort(reverse=True)
        #return arr
        for i in range(26):
            if arr[i] == 0:
                break
            pushes += arr[i] * (((i)//8)+1)
        return pushes


