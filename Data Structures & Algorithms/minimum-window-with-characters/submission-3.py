class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(t) > len(s):
            return ""

        hashMapA = {}  # Target counts from t
        hashMapB = {}  # Current window counts from s

        for c in t:
            hashMapA[c] = hashMapA.get(c, 0) + 1

        # Use sliding window to get the solutoin
        def isvalid():
            for i in hashMapA:
                if i not in hashMapB:
                    return False
                if hashMapA[i] > hashMapB[i]:
                    return False
            return True 

        left = 0
        result = ''
        compare = float('inf')
        for right in range(len(s)):
            if s[right] not in hashMapB:
                hashMapB[s[right]] = 0
            hashMapB[s[right]] +=1
            while isvalid():
                hashMapB[s[left]] -= 1
                if compare > (right+left-1):
                    result = s[left:right+1]
                left +=1

        return result
