class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Brute force
        # take the first string out of the loop
        # Have an index i to check for how many characters
        i = 0
        first = strs[0]
        while i < len(strs[0]):
            i+=1
            for j in range(1, len(strs)):
                if strs[j][0:i] != first[0:i]:
                    print('test')
                    return first[0:i-1]
                continue
        return first

