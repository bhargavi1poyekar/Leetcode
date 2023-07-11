# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        queue=deque([root])
        averages=[]
        while queue:
            level_sum=0
            count=len(queue)
            for _ in range(len(queue)):
                node=queue.popleft()
                level_sum+=node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            
            averages.append(level_sum/count)

        return averages

