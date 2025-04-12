class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        Understand:

        beginWord to endWord using wordList. 

        adjancent pair of words -> in sequence differ by single letter. 
        0 if no sequence exists. 

        Questions:
        endWord needs to be in wordList?
        all words length -> same
        words are unique. 

        return: number of words in sequence. 

        Match:
        Graph BFS

        But how to find neighbors. 

        Create an intermediate words from substituting each letter from words in the wordList with *. 

        Store these intermediate words as key and all the words, that can form this intermediate word will be the values. 

        Now, in bfs, when we need to find neighbors. we create intermediate words of the current word. And then get the neighbors of that intermediate word (values) from the hash. 
        '''

        if endWord not in wordList:
            return 0

        word_length = len(beginWord)
        graph = defaultdict(list)

        for word in wordList:
            for i in range(word_length):
                inter_word = word[:i] + '*' + word[i+1:]
                graph[inter_word].append(word)
        
        queue = deque([(beginWord, 1)])
        seen = {beginWord}

        while queue:
            word, count = queue.popleft()

            if word == endWord:
                return count

            for i in range(word_length):
                inter_word = word[:i] + '*' + word[i+1:]
            
                for nghbr in graph[inter_word]:
                    if nghbr not in seen:
                        seen.add(nghbr)
                        queue.append((nghbr, count + 1))
        
        return 0

        '''
        Time Complexity: O(M^2×N)
        where M is the length of each word and N is the total number of words in the input word list.

        Space Complexity -> same
        '''

