class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = {}
        result = []
        for i in strs:
            #sort = sorted(''.join(i))
            sort = ''.join(sorted(i))  # sort is now a string
            if sort not in check:
                check[sort] = []
            check[sort].append(i)
        return list(check.values())           
