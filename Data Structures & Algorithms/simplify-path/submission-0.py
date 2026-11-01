class Solution:

  def simplifyPath(self, path: str) -> str:
    stack = []
    curr = ""

    # Adding a trailing '/' ensures the final component is processed
    for char in path + "/":
      if char == "/":
        if curr == "..":
          if stack:
            stack.pop()
        elif curr != "" and curr != ".":
          stack.append(curr)

        # Reset accumulator for the next component
        curr = ""
      else:
        curr += char

    return "/" + "/".join(stack)