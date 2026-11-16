# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        result = [0]
        # Use bfs, dfs dont work 
        def dfs(root):
            if root is None:
                return
            if root.left or root.right:
                result[0] +=1
            print(result)
            dfs(root.right)
            dfs(root.left)    
        dfs(root)
        return result[0]