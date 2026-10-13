class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Using prefixSum as the key, and value is how many times it has counted beofre
        # prefix[j] - prefix [i] = k
        # prefix[j] - k = prefix[i]
        # The current total + the number of times prefix[i] has occured will give us
        # the solution
        prevSum = 0
        result = 0
        prefixSum = {0:1}
        for i in range(len(nums)):
            currSum = nums[i] + prevSum
            prevSum = currSum
            if currSum not in prefixSum:
                prefixSum[currSum] = 0
            potential = currSum - k
            if potential in prefixSum:
                result += prefixSum[potential]
            prefixSum[currSum] +=1
        return result
