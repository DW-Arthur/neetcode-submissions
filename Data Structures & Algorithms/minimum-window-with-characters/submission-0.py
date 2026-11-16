class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        left = 0
        hashMapA = {}  # Target counts from t
        hashMapB = {}  # Current window counts from s
        result = ''
        compare = float('inf')

        for i in t:
            hashMapA[i] = hashMapA.get(i, 0) + 1

        # Helper to check if window has all required character frequencies
        def is_valid():
            for char in hashMapA:
                if hashMapB.get(char, 0) < hashMapA[char]:
                    return False
            return True

        for right in range(len(s)):
            # 1. Expand: Add s[right] to window map
            char_r = s[right]
            hashMapB[char_r] = hashMapB.get(char_r, 0) + 1

            # 2. Shrink: While window is valid, record best & move left forward
            while is_valid():
                if (right - left + 1) < compare:
                    compare = right - left + 1
                    result = s[left:right + 1]

                # Remove s[left] from window before advancing left
                char_l = s[left]
                hashMapB[char_l] -= 1
                left += 1

        return result