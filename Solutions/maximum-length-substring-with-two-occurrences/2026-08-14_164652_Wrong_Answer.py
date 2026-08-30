# Problem: Maximum Length Substring With Two Occurrences
# Status: Wrong Answer
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-08-14_164652 UTC
# URL: https://leetcode.com/submissions/detail/2106828938/

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        max_len = 0
        str_len = len(s)
        left, right = 0, 0
        my_dict = {}
        #loop to traverse over the string

        while right < str_len:
            my_dict[s[right]] = my_dict.get(s[right], 0) + 1
            if my_dict[s[right]] <= 2:
                right += 1
            else:
                max_len = right - left
                my_dict[s[left]] -= 1
                left += 1
                right += 1

        return max_len