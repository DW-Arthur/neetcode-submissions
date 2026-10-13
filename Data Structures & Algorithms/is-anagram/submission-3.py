class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        test1 = dict()
        test2 = dict()
        for i in s:
            if i not in test1:
                test1[i] = 0
            test1[i] +=1
        for i in t:
            if i not in test2:
                test2[i] = 0 
            test2[i] +=1
        return test1 == test2