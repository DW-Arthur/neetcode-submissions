class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = {}
        second = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i not in first:
                first[i] = 0
            first[i] +=1
        for i in t:
            if i not in second:
                second[i] = 0
            second[i] +=1
        return first == second
            