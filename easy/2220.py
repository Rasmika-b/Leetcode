class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        count = 0
        while start or goal:
            if start%2 != goal%2:
                count += 1
            start = start//2
            goal = goal//2
        return count
        