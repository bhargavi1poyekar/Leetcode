# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return 0
        
        Q = deque([root])
        avgs = []

        while Q:
            length = len(Q)
            level = []
            for _ in range(length):
                node = Q.popleft()
                level.append(node.val)
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
                
            avg = sum(level)/len(level)
            avgs.append(avg)
        
        return avgs
        