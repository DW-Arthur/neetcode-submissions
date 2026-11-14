class Solution:

  def checkInclusion(self, s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
      return False

    s1freq = {}
    for char in s1:
      s1freq[char] = s1freq.get(char, 0) + 1

    left = 0
    while left + len(s1) <= len(s2):
      s2freq = {}
      for i in range(left, left + len(s1)):
        char = s2[i]
        s2freq[char] = s2freq.get(char, 0) + 1

      if s2freq == s1freq:
        return True

      left += 1

    return False