class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        grp=[]
        hash_map={}
        count=0
        
        for word in strs:
            word_sorted=''.join(sorted(word))
            
            if word_sorted in hash_map:
                grp[hash_map[word_sorted]].append(word)
            else:
                grp.append([word])
                hash_map[word_sorted]=count
                count+=1
            
        
        return grp