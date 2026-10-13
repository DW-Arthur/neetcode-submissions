class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #naive solution,
        count = {}
        for i in nums:
            if i not in count:
                count[i] = 0
            count[i] +=1
        # sort the dictionary based on the values
         # Sort by frequency, get the top k keys
        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)

        # Extract only the keys (numbers), not the frequencies
        return [item[0] for item in sorted_items[:k]]
            