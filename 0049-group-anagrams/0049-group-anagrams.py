class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        grp=[]
        hash={}
        grp_idx=0

        for i in range(len(strs)):
            word = ''.join(sorted(strs[i]))
        
            if word not in hash:
                grp.append([strs[i]])
                hash[word]=grp_idx
                grp_idx+=1
            else:
                grp[hash[word]].append(strs[i])

        
        return(grp)


        