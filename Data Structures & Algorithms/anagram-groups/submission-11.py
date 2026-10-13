class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use ord function
        # Time and Space complexity compared to brute force
        # Time: O(N), Space: O(N) BruteForce
        # Time: O(N), Space: O(N) ord operation
        cache = {}
        # Convert string to ord and put it as tuple to make it immutable, put it as key
        # If other string's ord conversion look the same, add it as the value
        def convert(string):
            count = [0] * 26
            for c in string:
                count[ord(c) - ord('a')] +=1
            return tuple(count)
        for string in strs:
            converted = convert(string)
            if converted not in cache:
                cache[converted] =[]
            cache[converted].append(string)
        result = []
        for key, value in cache.items():
            result.append(value)
        return result
        