class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        def find_nghbrs(gene):
            nghbrs = []
            for i in range(len(gene)):
                for choice in ['A', 'C', 'G', 'T']:
                    new_gene = gene[:i] + choice + gene[i+1:]
                    nghbrs.append(new_gene)
                    
            return nghbrs

        seen = {startGene}
        queue = deque([(startGene, 0)])

        while queue:
            gene, steps = queue.popleft()

            if gene == endGene:
                return steps
            
            for new_gene in find_nghbrs(gene):
                if new_gene in bank and new_gene not in seen:
                    seen.add(new_gene)
                    queue.append((new_gene, steps+1))

        return -1