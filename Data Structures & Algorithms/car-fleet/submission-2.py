class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        for i in range (len(position)):
            pairs.append((position[i], speed[i]))
        pairs.sort(reverse= True)
        prev = (target - pairs[0][0])/ pairs[0][1]
        result = 1
        for i, j in pairs:
            curr = (target - i)/ j
            if curr > prev:
                prev = curr
                result +=1
        return result


        