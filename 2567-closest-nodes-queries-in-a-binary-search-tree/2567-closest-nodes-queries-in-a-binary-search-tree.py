# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            bst.append(root.val)
            inorder(root.right)
        
        def binarySearch(array,target):
            left,right=0,len(array)

            while left<right:
                mid=(left+right)//2
                if array[mid]>=target:
                    right=mid
                else:
                    left=mid+1
            
            return left
        
        bst=[]
        inorder(root)
        ans=[]
        for query in queries:
            index=binarySearch(bst,query)
            
            if 0<=index<len(bst) and bst[index]==query:
                ans.append([query,query])
            else:
                temp=[-1,-1]
                if index>0:
                    temp[0]=bst[index-1]
                if index<len(bst):
                    temp[1]=bst[index]
                ans.append(temp)
        return ans
            






            

            