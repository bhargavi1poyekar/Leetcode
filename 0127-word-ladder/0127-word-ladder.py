class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        length = len(beginWord)
        graph = defaultdict(list)

        for word in wordList:
            for i in range(length):
                intermediate_word = word[:i] + '*' + word[i+1:]
                graph[intermediate_word].append(word)
        
        queue = deque([(beginWord, 1)])
        seen = {beginWord}

        while queue:
            word, seq = queue.popleft()

            if word == endWord:
                return seq
            
            for i in range(length):
                inter = word[:i] + '*' + word[i+1:]
                for nghbr in graph[inter]:
                    if nghbr not in seen:
                        seen.add(nghbr)
                        queue.append((nghbr, seq+1))
        
        return 0





