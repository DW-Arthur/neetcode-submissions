class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for string in strs:
            result += str(len(string)) + '#' + string
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = s.find('#', i)        # first '#' at or after i is the separator
            length = int(s[i:j])      # digits between i and the separator
            start = j + 1
            result.append(s[start:start + length])
            i = start + length        # jump to the next chunk
        return result


