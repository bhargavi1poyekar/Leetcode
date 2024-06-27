class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        nodes = {}
        for u, v in edges:
            if u not in nodes:
                nodes[u]=1
            else:
                nodes[u]+=1
            if v not in nodes:
                nodes[v]=1
            else:
                nodes[v]+=1
        
        
        total_nodes = len(nodes)

        for i in nodes:
            if nodes[i] == total_nodes-1:
                return i
            
        