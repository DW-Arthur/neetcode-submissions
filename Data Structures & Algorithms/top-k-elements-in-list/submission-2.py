class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        result = []
        for i in nums:
            if i in count:
                count[i] +=1
            else:
                count[i] = 1
        print(count)
        for i, j in count.items():
            result.append((j, i))   # store (frequency, number)
        result.sort()
        return [num for freq, num in result[-k:]]