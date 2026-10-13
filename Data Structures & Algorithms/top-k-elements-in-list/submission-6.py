class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Brute force hashmap
        counter = {}
        for i in nums:
            if i not in counter:
                counter[i] = 0
            counter[i] += 1
        # Sort the counter based on values
        result = []
        arr = []
        for num, cnt in counter.items():
            arr.append([cnt,num])
        arr.sort()
        for i in range(0,k):
            result.append(arr.pop()[1])
        return result