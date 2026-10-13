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
        bucket = {}
        for num, cnt in counter.items():
            if cnt not in bucket:
                bucket[cnt] = []
            bucket[cnt].append(num)
        # Iterate the bucket array from the back
        for freq in range(len(nums), 0, -1):
            if freq in bucket:
                for num in bucket[freq]:
                    result.append(num)
                    if len(result) == k:
                        return result