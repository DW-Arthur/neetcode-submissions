# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Use dfs or bfs
        # DFS method
        def dfs(p, q):
            if not p and not q:
                return True
            # Find a way to find if one is None and other is not None
            # 2. Only one node is None (or values differ) -> not identical
            if not p or not q or p.val != q.val:
                return False
            left = dfs(p.left, q.left)
            right = dfs(p.right, q.right)
            return left and right
        return dfs(p,q)