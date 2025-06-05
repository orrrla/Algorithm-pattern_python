# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result=[]
        queue = deque([root])
        flag = True
        while len(queue)>0:
            cur_level = deque([])
            for _ in range(len(queue)):
                node = queue.popleft()
                if flag:
                    cur_level.append(node.val)
                else:
                    cur_level.appendleft(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            flag = not flag
            result.append(list(cur_level))
        return result