# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -inf
        def dfs(node):
            if node is None:
                return 0
            l_max = dfs(node.left)
            r_max = dfs(node.right)
            nonlocal ans
            ans = max(ans,l_max+r_max+node.val)
            return max(max(l_max,r_max)+node.val,0)
        dfs(root)
        return ans

