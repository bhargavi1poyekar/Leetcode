class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        count = Counter()

        para = re.split(r'\W+', paragraph.lower())

        for word in para:
            if word != '':
                count[word.lower()] += 1
        
        banned = set(banned)
        # print(para)
        
        max_heap = []
        for word in count:
            # print(word)
            if word not in banned:
                # print(max_heap)
                heapq.heappush(max_heap, (-count[word], word))
        
        return max_heap[0][1]


        
