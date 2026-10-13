class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums)+1)] 
        count = {}
        for i in nums:
            if i not in count:
                count[i] =0
            count[i] +=1
        for value, freq in count.items():
            bucket[freq].append(value)
        result = []
        for i in range(len(bucket)-1, 0, -1):
            for j in bucket[i]:
                if len(result) < k:
                    result.append(j)
                else:
                    return result
        return result

        