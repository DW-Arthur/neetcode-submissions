class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        test = dict()
        def helper(s):
            count = [0] * 26
            for c in s:
                index = ord(c) - ord('a')
                count[index] +=1
            return count
        for s in strs:
            n = helper(s)
            if tuple(n) not in test:
                test[tuple(n)] = [s]
            else:
                test[tuple(n)].append(s)
        return list(test.values())