class Solution(object):
    def findMaxAverage(self, nums, k):
        curr = sum(nums[:k])
        best = curr
        for i in range(k, len(nums)):
            curr = (curr + nums[i] - nums[i-k])
            best = max(best, curr)
        
        return best/float(k)
        