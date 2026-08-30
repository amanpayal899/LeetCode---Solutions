# Problem: Smallest Missing Multiple of K
# Status: Accepted
# Language: python3
# Runtime: 0 ms
# Memory: 19.3 MB
# Submitted: 2026-08-25_175540 UTC
# URL: https://leetcode.com/submissions/detail/2120008854/

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        hash_table = set()
        for i in nums:
            hash_table.add(i)
        result = k
        count = 2
        while result in hash_table:
            result = k*count
            count += 1
        return result
        
