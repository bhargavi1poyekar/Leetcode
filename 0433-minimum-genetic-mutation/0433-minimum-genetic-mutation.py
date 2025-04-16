class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        '''
        Understand:
        string -> 8 char long _> choices A, C, G T

        startGene to endGene. 
        1 mutation -> 1 char changed. 

        geneBank -> valid genes. 

        return -> min num of mutations -> from startGene to endGene
        not possible -> return -1

        start might not be in bank

        can startGene == endGene -> return 0? 
        only these chars -> A C G T. in start and end?
        lentgh of both start and end would be same?

        Match:

        BFS Traversal -> to get min mutations. 

        Plan:

        Normal BFS traversal using queue. 
        Here the problem is that we have to create the graph neighbors dynamically. 

        So we generate neighbors using what we know. 
        8 chars -> and 4 possibilities for each 
        so in total 4 ** 8 total possibilities. -> but this is constant fixed. 
        '''

        def get_neighbrs(gene):
            nghbr_genes = []
            for i in range(8):
                for char in ['A', 'C', 'G', 'T']:
                    inter_gene = gene[:i] + char + gene[i+1:]
                    nghbr_genes.append(inter_gene)

            return nghbr_genes 

        if endGene not in bank:
            return -1

        queue = deque([(startGene, 0)])
        seen = {startGene}

        while queue:
            gene, num_mut = queue.popleft()

            if gene == endGene:
                return num_mut
            
            neighbrs = get_neighbrs(gene)
            for nghbr in neighbrs:
                if nghbr in bank and nghbr not in seen:
                    seen.add(nghbr)
                    queue.append((nghbr, num_mut + 1))
            
        return -1

        '''
        Time Complexity: O(B) -> bank.length
        Space: O(1) -> constant for the 4 ** 8

        '''