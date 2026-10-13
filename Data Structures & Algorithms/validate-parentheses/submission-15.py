class Solution:
    def isValid(self, s: str) -> bool:
        #put everything in a queue, if encounter a closing bracket
        #pop the stack and see if it fits
        queue = []
        check = {'}':'{', ']': '[', ')': '('}
        for i in s:
            if i in check:
                if not queue or queue.pop() != check[i]:
                    return False
            else:
                queue.append(i)
        return not queue

        
        