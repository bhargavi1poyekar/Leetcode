"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    seen = {}
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return node
        
        if node in self.seen:
            return self.seen[node]
        
        clone = Node(node.val, [])
        self.seen[node] = clone

        if node.neighbors:
            clone.neighbors = [self.cloneGraph(nghbr) for nghbr in (node.neighbors)]
        
        return clone
