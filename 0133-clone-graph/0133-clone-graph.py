"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

'''
Understand: Deep copy of graph, without making any references to original graph. All the neighbours should be the copy of the neighbors. 

What is given graph is empty -> then return None. 

Match:
Graph -> BFS/DFS -> DFS

PLan:
hash -> clone of each nodes. 

for every node -> that we traverse using dfs. 

dfs(node):
    if not node:
        return None
    if node in clone:
        return clone[node]
    
    clone_node = Node(node.val)
    clone[node] = clone_node

    do the dfs for each neighbor.  
'''

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.clone = {}

        def dfs(node):
            if not node:
                return None
            
            if node in self.clone:
                return self.clone[node]
            
            clone_node = Node(node.val)
            self.clone[node] = clone_node

            clone_node.neighbors = [dfs(nghbr) for nghbr in node.neighbors]

            return self.clone[node]
        
        return dfs(node)


        