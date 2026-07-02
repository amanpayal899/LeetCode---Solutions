class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        my_stack = []
        n = len(nums)
        result = [-1]*n
        for i in range(n-1, -1, -1):
            while my_stack and my_stack[-1] <= nums[i]:
                my_stack.pop()
            my_stack.append(nums[i])

        for j in range(n-1, -1, -1):
            while my_stack and my_stack[-1] <= nums[j]:
                my_stack.pop()
            if my_stack:
                result[j] = my_stack[-1]
            my_stack.append(nums[j])
        return result

