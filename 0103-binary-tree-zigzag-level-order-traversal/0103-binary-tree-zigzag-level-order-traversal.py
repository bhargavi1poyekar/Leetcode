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
        
        Q = deque([root])
        zig_zag = []
        level_number = 1
        while Q:
            level = []
            for _ in range(len(Q)):
                node = Q.popleft()
                level.append(node.val)
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
                
            if level_number % 2 == 1:
                zig_zag.append(level)
            else:
                zig_zag.append(level[::-1])
            level_number += 1
        
        return zig_zag
            
        
        