# Problem: Minimum Number of Pushes to Type Word II
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-07-31_202703 UTC
# URL: https://leetcode.com/submissions/detail/2089279249/

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
            pushes += arr[i] * (((i+1)//9)+1)
        return pushes


