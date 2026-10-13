class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort each string, then use dictionary to check if the current string 
        # is in the dictionary or not
        check = defaultdict(list)
        for i in strs:
            s = "".join(sorted(i))
            check[s].append(i)
        return list(check.values())
                
        

