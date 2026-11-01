class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        while left <=right:
            mid = (left + right)//2
            product = mid * mid
            if product < x:
                left  = mid +1
            elif product > x:
                right = mid -1
            else:
                return mid
        return mid-1