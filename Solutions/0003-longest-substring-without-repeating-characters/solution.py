class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_dict = {}
        l, r = 0, 0
        n = len(s)
        maxi = 0
        while r<n:
            while r < n and (s[r] not in my_dict or my_dict[s[r]] < l):
                my_dict[s[r]] = r
                r+=1
            maxi = max(maxi, r - l)
            if r > n-1:
                continue
            l = my_dict[s[r]] + 1
        return maxi



