class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()
        for i in range(len(nums)):
            if nums[i] not in s:
                s.add(nums[i])
            else:
                return nums[i]