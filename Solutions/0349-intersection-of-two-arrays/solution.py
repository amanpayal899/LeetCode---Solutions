class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        my_set = set()
        for i in nums1:
            my_set.add(i)
        for i in nums2:
            if i in my_set:
                result.append(i)
                my_set.remove(i)

        return result
