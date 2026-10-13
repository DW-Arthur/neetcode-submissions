class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Take the first string as our reference
        for i in range(len(strs[0])):
            char = strs[0][i]
            
            # Compare this character with the character at index i in all other strings
            for string in strs[1:]:
                # If the string is too short OR characters mismatch, return immediately
                if i == len(string) or string[i] != char:
                    return strs[0][:i]
        
        # If we finished the loop without mismatch, the entire first string is the prefix
        return strs[0]
            

        