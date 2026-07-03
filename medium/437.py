# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        self.paths = 0
        self.pathSums = defaultdict(int)
        self.pathSums[0] = 1

        def dfs(r, currSum):
            if r is None:
                return 
            currSum += r.val
            self.paths += self.pathSums[currSum - targetSum]
            self.pathSums[currSum] += 1
            if r.right:
                dfs(r.right, currSum)
            if r.left:
                dfs(r.left, currSum)
            self.pathSums[currSum] -= 1
        
        dfs(root, 0)
        return self.paths

        