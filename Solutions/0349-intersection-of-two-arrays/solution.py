class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        l1 = len(nums1)
        l2 = len(nums2)
        i, j = 0, 0
        result = []
        while (i<l1 and j<l2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                while i<l1 and nums1[i] == result[-1]:
                    i+=1
                while j<l2 and nums2[j] == result[-1]:
                    j+=1
            else:
                if nums1[i]<nums2[j]:
                    i+=1
                elif nums2[j]<nums1[i]:
                    j+=1
                else:
                    i+=1
                    j+=1

        return result
