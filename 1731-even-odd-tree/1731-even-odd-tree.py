# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:

        queue = deque([root])

        level_idx = 0

        while queue:

            length = len(queue) # getting the length, before appending to queue

            # Append to the end of level
            if level_idx % 2 == 0:
                # increasing order, last element should be max
                queue.append(TreeNode(float('inf')))
            else:
                # increasing order, last element should be min
                queue.append(TreeNode(float('-inf')))
            
            for _ in range(length):
                node = queue.popleft()

                if level_idx % 2 == 0:
                    # check wether val is evem or decreasing order
                    if node.val % 2 != 1 or node.val >= queue[0].val:
                        return False 
                
                elif level_idx % 2 == 1:
                    # check wether val is odd or increasing order
                    if node.val % 2 != 0 or node.val <= queue[0].val:
                        return False 
                    
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                

            level_idx += 1
            queue.popleft()
    
        return True