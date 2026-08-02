class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        count, res = 0, 0
        for i in s:
            if i == "(":
                count += 1
                res = max(res, count)
            elif i == ")":
                count -= 1
        
        return res