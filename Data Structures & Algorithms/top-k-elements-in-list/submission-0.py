class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #naive solution,
        count = {}
        for i in nums:
            if i not in count:
                count[i] = 0
            count[i] +=1
        # sort the dictionary based on the values
        arr = []
        for num, cnt in count.items():
            arr.append([cnt,num])
        arr.sort()
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
        