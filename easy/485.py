class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        curr = 0
        for n in nums:
            if n:
                curr = curr+1
                if curr > res:
                    res = curr
            else:
                curr = 0
        return res


        