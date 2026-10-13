class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Using ord
        # ord(character) - ord(a) = result
        # return result 
        # Maybe having a tuple of the ord character as the key
        # key = 'act' as ord tuple 
        # If the string has the same characters as tuple key, add the index as the value to the key
        copy = {}
        for i in strs:
            count = [0] * 26
            for c in i:
                count[ord(c) - ord('a')] += 1
            if tuple(count) not in copy:
                copy[tuple(count)] = []
            copy[tuple(count)].append(i)
        return list(copy.values())
        