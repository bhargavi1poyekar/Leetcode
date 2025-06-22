class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        graph = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                inter_word = word[:i] + '*' + word[i+1:]
                graph[inter_word].append(word)
        
        queue = deque([(beginWord, 1)])
        seen = {beginWord}

        while queue:
            word, steps = queue.popleft()

            if word == endWord:
                return steps

            for i in range(len(word)):
                inter_word = word[:i] + '*' + word[i+1:]
                for nghbr in graph[inter_word]:
                    if nghbr not in seen:
                        seen.add(nghbr)
                        queue.append((nghbr, steps + 1))
        
        return 0

