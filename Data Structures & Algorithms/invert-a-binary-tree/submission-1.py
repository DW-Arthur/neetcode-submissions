# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        # Assume that the recursion returns the right node upwards
        tmpRight = self.invertTree(root.right)
        tmpLeft = self.invertTree(root.left)
        root.left = tmpRight
        root.right = tmpLeft
        return root