class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0

        wordlen=len(beginWord)
        graph=defaultdict(list)

        for word in wordList:
            for i in range(wordlen):
                graph[word[:i]+'*'+word[i+1:]].append(word)
        
        seen=set()
        queue=deque([(beginWord,1)])

        while queue:
            node,steps=queue.popleft()
            for i in range(wordlen):
                inter=node[:i]+'*'+node[i+1:]
                for nghbr in graph[inter]:
                    if nghbr==endWord:
                        return steps+1
                    if nghbr not in seen:
                        seen.add(nghbr)
                        queue.append((nghbr,steps+1))
        return 0