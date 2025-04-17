class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        '''
        Understand:

        Given -> n cities -> numbered from 0 to n-1 
        and n-1 roads -> only one way to travel betwen 2 cities. 

        Unidirectional. 

        roads -> connections. [a, b] -> road from a to b.

        want to travel to city 0. 

        reorienting some roads _> so each city can visit city 0. 
        return min edges changed. guaranteed that each city cna reach 0. 

        Match: DFS traversal. 

        Plan:
        
        We consider all roads as unidirectional. 
        and store the real roads as tuple in a set/ list.  

        Now, we traverse from city 0. 

        If we find a road that is present in real road -> we need to reverse this road. because right now we are travelling from 0 to other cities. So current road is going away from 0. so we need to reverse it. 

        Keep count of such roads. 
        '''

        graph = defaultdict(list)
        roads = set()

        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
            roads.add((a, b))
        
        seen = {0}
        self.reorder = 0

        def dfs(city):
            for nghbr in graph[city]:
                if nghbr not in seen:
                    if (city, nghbr) in roads:
                        self.reorder += 1    
                    seen.add(nghbr)
                    dfs(nghbr)
        
        dfs(0)
        return self.reorder

        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        
        '''
                
