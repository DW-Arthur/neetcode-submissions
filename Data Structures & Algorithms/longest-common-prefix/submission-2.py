from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Edge case: handle empty list
        if not strs:
            return ""

        prefix_len = 0

        # Loop through the length of the first string (1-indexed for slice lengths)
        for i in range(1, len(strs[0]) + 1):
            target_slice = strs[0][0:i]
            all_match = True

            # Compare target_slice against every string in the list
            for string in strs:
                # If a string is shorter than i or its prefix doesn't match
                if len(string) < i or string[0:i] != target_slice:
                    all_match = False
                    break  # Stop checking this slice length

            # Only increment if ALL strings matched this slice
            if all_match:
                prefix_len = i
            else:
                break  # Stop expanding the prefix length

        return strs[0][0:prefix_len]