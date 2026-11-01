class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        mid =1
        while left <=right:
            mid = (left + right)//2
            product = mid * mid
            if product < x:
                left  = mid +1
            elif product > x:
                right = mid -1
            else:
                return mid
        if mid !=1:
            return mid-1
        return 1