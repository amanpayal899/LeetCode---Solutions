# Problem: Destroying Asteroids
# Status: Accepted
# Language: python3
# Runtime: 1122 ms
# Memory: 34.8 MB
# Submitted: 2026-05-31_181646 UTC
# URL: https://leetcode.com/submissions/detail/2018414831/

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        def merge_sorted_arr(left, right):
            len1 = len(left)
            len2 = len(right)
            i, j = 0, 0
            result = []
            while i<len1 and j<len2:
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            while i < len1:
                result.append(left[i])
                i += 1
            while j < len2:
                result.append(right[j])
                j += 1
            return result
        def merge_sort(arr):
            length = len(arr)
            if length <= 1:
                return arr
            mid = length//2
            left_arr = arr[:mid]
            right_arr = arr[mid:]
            left_arr = merge_sort(left_arr)
            right_arr = merge_sort(right_arr)
            return merge_sorted_arr(left_arr, right_arr)
        asteroids = merge_sort(asteroids)
        for i in asteroids:
            if i > mass:
                return False
            mass += i
        return True
