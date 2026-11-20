# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Can I use bfs here using level traversal?
        # Using recursion is way easier
        def dfs(root):
            if root is None:
                return 0, True
            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)
            if rightHeight >= leftHeight:
                diff = abs(rightHeight -leftHeight)
                
            else:
                diff = abs(leftHeight - rightHeight)
            if diff >1:
                return diff, False
            return max(leftHeight, rightHeight)