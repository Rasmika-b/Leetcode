class Solution(object):
    def maxOperations(self, nums, k):
        nums.sort()
        count = 0
        i = 0
        j = len(nums)-1
        while i<j:
            if nums[i]+nums[j]==k:
                count = count+1
                i = i+1
                j = j-1
            elif nums[i]+nums[j]>k:
                j = j-1
            else:
                i = i+1

        return count
        