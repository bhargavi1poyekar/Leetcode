class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        '''
        Understand:

        Given: arr of strs -> group anagrams. 
        Return in any order. 

        Match: Hash -> sort the string and keep it as a key in hash. Then sort
        '''

        anagrams = defaultdict(list)
        for string in strs:
            sorted_str = sorted(string)
            anagrams[tuple(sorted_str)].append(string)
        
        ans = []
        for ang in anagrams:
            ans.append(anagrams[ang])
        
        return ans




