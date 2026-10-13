class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = dict()
        count2 = dict()
        for i in s:
            if i not in count1:
                count1[i] =0
            count1[i] +=1
        for i in t:
            if i not in count2:
                count2[i] =0
            count2[i] +=1
        return count1 == count2
