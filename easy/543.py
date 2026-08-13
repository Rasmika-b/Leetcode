# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        
        self.maxdia = 0

        def maxheight(root):
            if not root:
                return 0
            
            left = maxheight(root.left)
            right = maxheight(root.right)

            self.maxdia = max(self.maxdia, left + right)

            return 1+max(left, right)
    
        maxheight(root)
        return self.maxdia