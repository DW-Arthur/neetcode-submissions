class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        first, last = 0, len(s)-1
        while first <last:
            tmp  = s[first]
            s[first] =s[last]
            s[last] = tmp
            first +=1
            last -=1
        return s
        