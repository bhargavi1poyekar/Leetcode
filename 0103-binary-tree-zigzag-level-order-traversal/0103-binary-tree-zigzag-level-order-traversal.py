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
        level=1
        queue=deque([root])
        ans=[]

        while queue:
            levelnodes=[]
            for _ in range(len(queue)):
                node=queue.popleft()
                levelnodes.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # print(levelnodes)
            if level%2==0:
                ans.append(levelnodes[::-1])
            else:
                ans.append(levelnodes)
            level+=1
        
        return ans
