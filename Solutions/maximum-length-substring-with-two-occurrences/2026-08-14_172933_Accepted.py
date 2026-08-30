# Problem: Maximum Length Substring With Two Occurrences
# Status: Accepted
# Language: python3
# Runtime: 3 ms
# Memory: 19.3 MB
# Submitted: 2026-08-14_172933 UTC
# URL: https://leetcode.com/submissions/detail/2106881268/

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
                max_len = max(max_len, right-left)
                while s[left]!=s[right]:
                    my_dict[s[left]] -= 1
                    left += 1
                    
                my_dict[s[left]] -= 1
                left += 1
                right += 1
                
        max_len = max(right-left, max_len)
        return max_len