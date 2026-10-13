class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Have a hasmap
        # go through the list, add the characters in the hashmap,
        # if there is a duplicate, reset the hasmap, and move the pointer 
        # to the last location
        check = {}
        result = 0
        start = 0

        for i, ch in enumerate(s):
            if ch in check and check[ch] >= start:
                start = check[ch] + 1
            check[ch] = i
            result = max(result, i - start + 1)

        return result
            
            