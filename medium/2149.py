class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i, j, ans = [], [], []
        for num in nums:
            if num>0:
                i.append(num)
            else:
                j.append(num)
        
        a, b = 0, 0

        while b < len(nums)//2:
            ans.append(i[a])
            a = a+1
            ans.append(j[b])
            b = b+1
        
        return ans
        