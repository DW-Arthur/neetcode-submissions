class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        result = 0
        while left <=right:
            mid = (left + right)//2
            product = mid * mid
            if product < x:
                left  = mid +1
                result = mid
            elif product > x:
                right = mid -1
            else:
                return mid
        return result 