# Problem: Longest Substring Without Repeating Characters
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-07-06_170710 UTC
# URL: https://leetcode.com/submissions/detail/2058335768/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        p1, p2 = 0, 0
        maxi = 0
        my_dict = {}
        while p2 < n:
            while p2 < n and s[p2] not in my_dict:
                my_dict[s[p2]] = p2
                p2 += 1
            maxi = max(maxi, p2-p1)
            if p2 == n:
                continue
            p1 = my_dict[s[p2]] + 1
            del my_dict[s[p2]]

        return maxi
