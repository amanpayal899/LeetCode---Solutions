class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        longest = 0
        for i in my_set:
            if i-1 not in my_set:
                current_sequence_count = 1
                x = 1
                while i + x in my_set:
                    current_sequence_count += 1
                    x += 1
                if current_sequence_count > longest:
                    longest = current_sequence_count
                
        return longest

