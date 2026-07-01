# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        def get_leaves(node):
            leaves = []
            def dfs(curr):
                if not curr:
                    return
                if not curr.left and not curr.right:
                    return leaves.append(curr.val)
                dfs(curr.left)
                dfs(curr.right)
            dfs(node)
            return leaves
    
        return get_leaves(root1) == get_leaves(root2)
        