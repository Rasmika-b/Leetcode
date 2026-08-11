class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        next_big_ele = {}
        stack = []

        for num in reversed(nums2):
            while stack and stack[-1] <= num:
                stack.pop()
            next_big_ele[num] = -1 if not stack else stack[-1]
            stack.append(num)
        
        return [next_big_ele[num] for num in nums1]