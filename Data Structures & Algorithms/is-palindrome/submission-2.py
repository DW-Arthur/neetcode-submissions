class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove all the space in the string and make everything case sensitive 
        # Remove the punctuations like ,.'
        # Remove everything
        newStr = ''
        for c in s:
             if c.isalnum():
                newStr += c.lower()
        left, right =0, len(newStr)-1
        while left < right:
            if newStr[left] != newStr[right]:
                return False
            left +=1
            right -=1
        return True
