class Solution:

  def decodeString(self, s: str) -> str:
    num = []  # Stack for repeat multipliers (k)
    char = []  # Stack for previous strings before '['
    curr_str = ''  # The string currently being built
    curr_num = 0  # Accumulator for multi-digit numbers

    for i in s:
      if i.isdigit():
        # Handles multi-digit numbers like "100"
        curr_num = curr_num * 10 + int(i)

      elif i == '[':
        # Save the current state before going deeper
        num.append(curr_num)
        char.append(curr_str)
        # Reset for the content inside this new set of brackets
        curr_num = 0
        curr_str = ''

      elif i == ']':
        # Pop multiplier and previous string context
        count = num.pop()
        prev_str = char.pop()
        # Combine: the outer context + repeated current segment
        curr_str = prev_str + (count * curr_str)

      else:
        # Standard alphabetical character
        curr_str += i

    return curr_str