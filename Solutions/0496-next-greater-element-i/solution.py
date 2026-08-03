class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l1 = len(nums1)
        l2 = len(nums2)
        result = []
        dictionary = {}
        for i in range(l2):
            dictionary[nums2[i]] = i
        
        for i in range(l1):
            curr = dictionary[nums1[i]]
            j = curr+1
            
            while j<l2:
                if nums2[j] > nums1[i]:
                    result.append(nums2[j])
                    break 
                j+=1
            if j==l2:
                result.append(-1)
            

        return result
