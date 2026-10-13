class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for string in strs:
            result += str(len(string)) + '#' + string
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        index = 0
        while index < len(s):
            # walk forward collecting digits until we hit '#'
            j = index
            length_str = ''
            while s[j] != '#':
                length_str += s[j]
                j += 1
            advance = int(length_str)

            # j is now the index of '#', so the string starts at j + 1
            string = s[j + 1:j + 1 + advance]
            result.append(string)
            index = j + 1 + advance
        return result


