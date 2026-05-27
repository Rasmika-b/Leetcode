class Solution(object):
    def productExceptSelf(self, nums):
        # arr =[]
        # for i in range(len(nums)):
        #     k=1
        #     for j in range(len(nums)):
        #         if i!=j:
        #             k = k * nums[j]
        #     arr.append(k)
        # return arr

        n = len(nums)
        res = [1]*n
        prefix=1
        suffix=1
        for i in range(len(nums)):
            res[i]=prefix
            prefix = prefix * nums[i]
        
        for j in range(n-1, -1, -1):
            res[j]= res[j]*suffix
            suffix = suffix * nums[j]
        
        return res

        