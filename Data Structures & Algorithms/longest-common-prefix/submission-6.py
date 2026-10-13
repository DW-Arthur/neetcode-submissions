class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Edge case: empty list or first string is empty
        if not strs or strs[0] == "":
            return ""

        # Loop from length 1 up to the full length of the first string
        for i in range(1, len(strs[0]) + 1):
            stringCompare = strs[0][:i]
            for j in range(1, len(strs)):
                # If strs[j] is shorter than i or prefix doesn't match
                if len(strs[j]) < i or stringCompare != strs[j][:i]:
                    return strs[0][:i-1]

        return strs[0]