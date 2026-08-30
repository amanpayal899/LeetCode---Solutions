# Problem: Valid Palindrome II
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-04-09_212601 UTC
# URL: https://leetcode.com/submissions/detail/1973966264/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        count = 0
        i = 0
        j = len(s)-1
        while(i<j):
            if s[i] != s[j]:
                count += 1
                if s[i+1]!=s[j]:
                    return False
                    
            i += 1
            j -= 1
        if count <= 1:
            return True
        else:
            return False