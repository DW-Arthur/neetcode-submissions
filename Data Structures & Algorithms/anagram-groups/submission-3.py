class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort each string, then use dictionary to check if the current string 
        # is in the dictionary or not
        check = {}
        for i in strs:
            s = "".join(sorted(i))
            if s in check:
                check[s].append(i)
            else: 
                check[s] = []
                check[s].append(i)
        return list(check.values())
                
        

