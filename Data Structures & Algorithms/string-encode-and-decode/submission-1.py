class Solution:

    def encode(self, strs: List[str]) -> str:
        # Add hashtag and length in front of each string
        result = ''
        for s in strs:
           result += str(len(s)) + "#" + s
        return result
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # Read length
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            # Extract the string
            res.append(s[j+1: j+1+length])
            i = j + 1 + length
        return res
            
