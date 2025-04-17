# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        '''
        Understand:

        Given 2 roots -> root and subRoot. 
        return true if subtree of root same as subRoot. else False

        We need to check if subtree of root is same as subRoot. 

        Match: isSame()
        and do dfs for root, and its children, to match with subRoot. 
        
        Plan: separate function to check if two trees are same. 

        if both roots are None -> then True
        but if one of them is None -> then False. 

        Else compare the root values, and check left and right children recursively. If all same, only then trees are equal. 

        Now for dfs -> we first compare current root with subRoot. If same return True. 
        else check for root.left and right. recursively. 

        If any of them matches -> return True. 
        '''
        def isSame(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            
            return root1.val == root2.val and isSame(root1.left, root2.left) and isSame(root1.right, root2. right)
        
        def dfs(root, subRoot):
            if not root:
                return False
            if isSame(root, subRoot): return True

            return dfs(root.left, subRoot) or dfs(root.right, subRoot)
        
        return dfs(root, subRoot)



            