class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        def find_nghbr(gene):
            ans = []
            # print(gene)
            for i in range(8):
                for char in ['A', 'C', 'G', 'T']:
                    new_gene = gene[:i] + char + gene[i+1:]
                    ans.append(new_gene)

            return ans 
                

        seen = {startGene}
        queue = deque([(startGene, 0)])

        while queue:
            gene, steps = queue.popleft()

            if gene == endGene:
                return steps
            
            for nghbr in find_nghbr(gene):
                # print(nghbr)
                if nghbr in bank and nghbr not in seen:
                    seen.add(nghbr)
                    queue.append((nghbr, steps+1))
        
        return -1