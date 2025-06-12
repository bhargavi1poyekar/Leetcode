# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        queue = deque([root])
        avgs = []

        while queue:
            sum = 0
            count = 0 
            for _ in range(len(queue)):
                node = queue.popleft()
                sum += node.val
                count += 1

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            avgs.append(sum / count)
        
        return avgs
                