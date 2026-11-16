class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(t) > len(s):
            return ""

        hashMapA = {}  # Target counts from t
        hashMapB = {}  # Current window counts from s

        for c in t:
            hashMapA[c] = hashMapA.get(c, 0) + 1

        have, need = 0, len(hashMapA)
        res_bounds = [-1, -1]
        min_len = float("inf")
        left = 0

        for right in range(len(s)):
            # 1. Expand: Add s[right] to window
            c = s[right]
            hashMapB[c] = hashMapB.get(c, 0) + 1

            # Check if this character just satisfied its required count
            if c in hashMapA and hashMapB[c] == hashMapA[c]:
                have += 1

            # 2. Shrink: While all required characters are satisfied (O(1) check)
            while have == need:
                # Save indices only (no string slicing inside loop)
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    res_bounds = [left, right]

                # Remove s[left] from window
                left_char = s[left]
                hashMapB[left_char] -= 1
                if left_char in hashMapA and hashMapB[left_char] < hashMapA[left_char]:
                    have -= 1
                left += 1

        l, r = res_bounds
        return s[l:r + 1] if min_len != float("inf") else ""