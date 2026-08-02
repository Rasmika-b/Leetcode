class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        sum0 = 0
        d = dict()
        d[0] = 1

        for i in range(len(nums)):
            sum0 = sum0 + nums[i]
            count = count + d.get(sum0-k,0)
            d[sum0] = d.get(sum0, 0)+1
        
        return(count)
        