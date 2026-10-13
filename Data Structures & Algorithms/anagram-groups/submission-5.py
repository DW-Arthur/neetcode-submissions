class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            sort = "".join(sorted(s))
            if sort not in res:
                res[sort] = []
            res[sort].append(s)
        print(res)
        return list(res.values())                
        

