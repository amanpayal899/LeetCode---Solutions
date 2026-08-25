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
        

