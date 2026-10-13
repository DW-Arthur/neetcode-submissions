class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        first, second = 0,0
        result = ''
        while first <len(word1) and second <len(word2):
            result += word1[first] + word2[second]
            first +=1
            second +=1
        if first == len(word1):
            result += word2[second:]
        elif second == len(word2):
            result += word1[first:]
        return result


        