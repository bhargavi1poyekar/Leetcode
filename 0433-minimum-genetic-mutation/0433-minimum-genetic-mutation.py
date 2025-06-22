class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        def find_nghbrs(gene):
            nghbrs = []
            for i in range(8):
                for ch in ['A', 'C', 'G', 'T']:
                    newgene = gene[:i] + ch + gene[i+1:]
                    nghbrs.append(newgene)
            
            return nghbrs

        queue = deque([(startGene, 0)])
        seen = {startGene}

        while queue:
            gene, steps = queue.popleft()

            if gene == endGene:
                return steps
            
            for nextGene in find_nghbrs(gene):
                if nextGene in bank and nextGene not in seen:
                    seen.add(nextGene)
                    queue.append((nextGene, steps + 1))
        
        return -1
