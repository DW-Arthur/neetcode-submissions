class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        def helper(s):
            count = [0] *26
            for i in s:
                count[ord(i) - ord('a')] +=1
            return count
        for s in strs:
            count = helper(s)
            if tuple(count) in freq:
                freq[tuple(count)].append(s)
            else:
                freq[tuple(count)] = []
                freq[tuple(count)].append(s)
        return list(freq.values())
        