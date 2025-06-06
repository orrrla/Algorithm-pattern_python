# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0,True
            lh,lb = dfs(root.left)
            rh,rb = dfs(root.right)
            cur_b = lb and rb and abs(lh-rh)<2
            return max(lh,rh)+1,cur_b
            
        return dfs(root)[1]