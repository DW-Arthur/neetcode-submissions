class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 2 dictionaries get the count, then compare countT and countS
        countS = {}
        countT = {}
        for i in s:
            if i in countS:
                countS[i] +=1
            else:
                countS[i] =0
        for i in t:
            if i in countT:
                countT[i] +=1
            else:
                countT[i] =0
        return countT == countS
        