class Solution:

    def encode(self, strs: List[str]) -> str:
        # Turn a list of strings in to a single string
        # The string could be a length of above 10, so 10#, the hashtag should be after
        # the number
        result = ''
        for string in strs:
            result += str(len(string)) + '#' + string
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i =0
        while i < len(s):
            length = ''
            for j in range(i, len(s)):
                if s[j] != '#':
                    length += s[j]
                else:
                    advance = int(length)
                    break
            # Once getting the int lenght
            result.append(s[j+1: j+advance+1])
            i = j+advance+1
        print(result)
        return result
