# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        '''
        Understand:

        Given: root of binary tree and targetSum
        Return num paths -> where sum of values along path == targetSUm
        
        Path doesnt need to start or end at root or leaf. -> but must go downwards.  

        QuesT:
        can the values -> be negative -> or 0?  -> Yes
        Duplicate Values -> Yes
        can a single node -> constitute as path? yes

        Match: Binary tree DFS. 
        And Hash to store the path sums. 

        Plan:
        Maintain a hash -> to store the sums and their count that we encounter. 
        hash[0] = 1 -> for single node.     
        self.num_paths. 

        in dfs(root, hash, currsum):
            if not root:
                return
            
            curr_sum += root.val
            num_paths += hash[curr_sum - targetSum]   # add num of times the required sum was present. 

            hash[curr_sum] += 1 # add curr sum to hash. 

            root.left(root.left, hash, curr_sum)
            root.right(root.right, hash, curr_sum)
            
            hash[curr_sum] -= 1


        '''
        self.num_paths = 0
        hash_count = Counter()
        hash_count[0] = 1

        def dfs(root, hash_count, curr_sum):
            if not root:
                return
            
            curr_sum += root.val
            self.num_paths += hash_count[curr_sum - targetSum]   # add num of times the required sum was present. 
            hash_count[curr_sum] += 1 # add curr sum to hash. 

            dfs(root.left, hash_count, curr_sum)
            dfs(root.right, hash_count, curr_sum)
            
            hash_count[curr_sum] -= 1
        
        dfs(root, hash_count, 0)
        return self.num_paths
        
        '''
        Time Complexity: O(n)
        Space Complexity: O(n)
        '''