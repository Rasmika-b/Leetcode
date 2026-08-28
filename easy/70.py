class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def climb(n):
            if n ==1:
                return 1
            if n == 2:
                return 2
            return climb(n-1)+climb(n-2)
        return climb(n)

#Time Limit Exceeded!
        