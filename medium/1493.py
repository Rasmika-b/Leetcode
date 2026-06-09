class Solution(object):
    def longestSubarray(self, nums):
        k = 1
        count = 0
        start, end = 0, 0
        while end<len(nums):
            if nums[end]==0:
                k = k-1
            while k<0:
                if nums[start]==0:
                    k = k+1
                start=start+1
            count = max(count, end-start+1)
            end = end+1
        return count-1