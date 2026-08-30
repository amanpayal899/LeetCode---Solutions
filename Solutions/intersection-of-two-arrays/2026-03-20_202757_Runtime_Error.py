# Problem: Intersection of Two Arrays
# Status: Runtime Error
# Language: python3
# Runtime: N/A
# Memory: N/A
# Submitted: 2026-03-20_202757 UTC
# URL: https://leetcode.com/submissions/detail/1954278942/

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        my_set = set()
        for i in range(0,len(nums1)):
            my_set.add(nums1[i])
        for i in range(0,len(nums2)):
            my_set.add(nums2[i])
        arr = []
        j=0
        for i in my_set:
            arr.append(i)
        for i in nums1:
            if(arr[j]!=i):
                arr.remove(i)
                j+=1
        j=0
        for i in nums2:
            if(arr[j]!=i):
                arr.remove(i)
                j+=1
        return arr
    
