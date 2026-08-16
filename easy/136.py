class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dictionary = {}
        for num in nums:
            dictionary[num] = dictionary.get(num, 0)+1
        for key, val in dictionary.items():
            if val == 1:
                return key
        