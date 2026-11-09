class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        current = ''
        result = 1
        # Do I have to make a counter 
        for i in s:
            if i in current:
                result = max(result, len(current))
                current = ''
            current += i
        return result