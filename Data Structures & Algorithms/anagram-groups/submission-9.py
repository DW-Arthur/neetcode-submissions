class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for s in strs:
            sorted_key = "".join(sorted(s))

            # If the key isn't in the dictionary yet, create it with an empty list
            if sorted_key not in anagram_map:
                anagram_map[sorted_key] = []
            
            # Now it's guaranteed to exist, so appending is safe
            anagram_map[sorted_key].append(s)

        return list(anagram_map.values())
        