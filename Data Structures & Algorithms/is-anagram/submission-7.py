class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 2 dictionaries get the count, then compare countT and countS
        countS = {}
        countT = {}
        for i in s:
            if i not in countS:
                countS[i] = 0
            countS[i] += 1
        for i in t:
            if i not in countT:
                countT[i] = 0
            countT[i] += 1 
        return countT == countS
        