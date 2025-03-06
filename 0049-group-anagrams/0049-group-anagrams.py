class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = defaultdict(list)

        for string in strs:
            anag = ''.join(sorted(string))
            anagrams[anag].append(string)
        
        answer = []
        for anagram in anagrams:
            answer.append(anagrams[anagram])
        
        return answer
