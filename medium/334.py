class Solution(object):
    def increasingTriplet(self, nums):
        # n = len(nums)
        # for i in range(n-2):
        #     for j in range(i+1, n-1):
        #         for k in range(j+1, n):
        #             if nums[i]<nums[j]<nums[k]:
        #                 return True
        # return False    

        first = second = float('inf')
        for i in nums:
            if i<=first:
                first = i
            elif i<=second:
                second = i
            else:
                return True
        return False    