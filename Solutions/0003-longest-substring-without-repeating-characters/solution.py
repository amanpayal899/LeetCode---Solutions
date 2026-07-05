class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        p1 = 0
        p2 = 0
        dq = deque()
        largest = 0
        while p2 < n:
            
            while p2 < n and (s[p2] not in dq):
                dq.append(s[p2])
                p2 += 1
                
            if p2 - p1 > largest:
                largest = p2 - p1
            p1 += 1
            dq.popleft()
        return largest
