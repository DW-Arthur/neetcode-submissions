class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Even removing 1 character doesn't guarantee the remaining string is a palindrome
        # I need to compare if it is palindrome
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                # Check in 2 differnet strings
                skip_left = s[left+1:right+1]
                skip_right = s[left:right]
                if skip_left == skip_left[::-1] or skip_right == skip_right[::-1]:
                    return True
                else:
                    return False
            left +=1
            right -=1
        return True