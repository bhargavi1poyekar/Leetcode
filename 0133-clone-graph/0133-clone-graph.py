"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.clone = {}
        def dfs(node):
            if not node:
                return node
            
            if node in self.clone:
                return self.clone[node]
            
            clone_node = Node(node.val, [])
            self.clone[node] = clone_node

            if node.neighbors:
                clone_node.neighbors = [dfs(nghbr) for nghbr in node.neighbors]
            
            return clone_node
        
        return dfs(node)

        
    
