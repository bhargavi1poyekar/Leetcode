class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        hm = defaultdict(int)
        res = []
        universal_set = set()

        for w in words2:
            s = set(w)
            for c in s:
                cnt = w.count(c)
                if c in hm:
                    hm[c] = max(hm[c], cnt)
                else:
                    hm[c] = cnt
                universal_set.add(c)
                
        for w in words1:
            flag = True
            for c in universal_set:
                if w.count(c) < hm[c]:
                    flag = False and flag
                else:
                    flag = True and flag
            if flag:
                res.append(w)
        return res