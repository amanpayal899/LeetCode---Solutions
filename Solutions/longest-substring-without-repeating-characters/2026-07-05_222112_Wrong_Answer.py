# Problem: Longest Substring Without Repeating Characters
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-07-05_222112 UTC
# URL: https://leetcode.com/submissions/detail/2057369624/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        p1 = 0
        p2 = 0
        
        largest = 0
        while p2 < n:
            my_set = set()
            while p2 < n and (s[p2] not in my_set):
                my_set.add(s[p2])
                p2 += 1
                
            if p2 - p1 > largest:
                largest = p2 - p1
            p1 = p2
            while my_set:
                my_set.pop()
        return largest