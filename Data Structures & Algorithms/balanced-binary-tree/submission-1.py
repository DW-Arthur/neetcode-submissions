# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # use dfs
        result =[1]
        def dfs(root):
            if root is None:
                return 0
            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)
            if leftHeight > rightHeight:
                diff = leftHeight - rightHeight
            else:
                diff = rightHeight - leftHeight
            if diff >1:
                result[0] = 0
            return 1+ max(leftHeight, rightHeight)
        dfs(root)
        print(result[0])
        if result[0] == 1:
            return True
        return False