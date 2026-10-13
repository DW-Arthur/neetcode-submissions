class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket Sort Frequencies
        bucket = [[] for i in range(len(nums) + 1)]
        # Assume this makes the bucket a list of length size nums
        counter = {}
        for i in nums:
            if i not in counter:
                counter[i] = 0
            counter[i] +=1
        # Counter key is now the number, value is now the frequencies
        result = []
        # This is how you add the bucket key as counts, value as the actual number
        for num, cnt in counter.items():
            bucket[cnt].append(num)
        # Iterate the bucket array from the back
        for i in range(len(bucket)-1, 0, -1):
            toBeAdded = bucket[i]
            for j in toBeAdded:
                result.append(j)
                if len(result) == k:
                    return result
