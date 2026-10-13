class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        first, second = 0,0
        result = ''
        while first <len(word1) and second <len(word2):
            result += word1[first] + word2[second]
            first +=1
            second +=1
        result += word1[first:] + word2[second:]
        return result


        