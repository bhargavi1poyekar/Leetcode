# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        queue = deque([root])
        level = 1
        max_level = 1

        max_sum = root.val
        while queue:
            sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if sum > max_sum:
                max_sum = sum
                max_level = level

            level += 1
        
        return max_level
        