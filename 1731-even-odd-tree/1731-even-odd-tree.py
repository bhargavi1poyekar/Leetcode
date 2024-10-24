# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        
        queue=deque([root])
        level=0

        while queue:
            length=len(queue)
            if level%2==0:
                queue.append(TreeNode(float('inf')))
            else:
                queue.append(TreeNode(float('-inf')))
            
            for _ in range(length):
                node=queue.popleft()
                # print(level,node.val,queue[0].val)
                if level%2==0: 
                    if node.val%2!=1 or node.val>=queue[0].val:
                        return False
                elif level%2==1: 
                    if node.val%2!=0 or node.val<=queue[0].val:
                        return False
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            level+=1
            queue.popleft()
        
        return True
                    

