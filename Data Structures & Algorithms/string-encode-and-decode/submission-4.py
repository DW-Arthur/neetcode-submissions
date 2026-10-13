class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        #add the lenght of the string, then the actual string
        for s in strs:
            result += str(len(s)) + '#' + s
        return result
    def decode(self, s: str) -> List[str]:
        "4#neet4#code4#love3#you"
        result = []
        i = 0
        while i <= len(s)-1:
            j = i
            while s[j] != '#':
                j +=1
            # get the number
            jump = int(s[i:j])
            first = j +1
            second = j + jump +1
            word = s[first:second]
            result.append(word)
            i = second
        return result
            

