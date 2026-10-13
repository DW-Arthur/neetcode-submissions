class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        for i in range(len(position)):
            pairs.append((position[i], speed[i]))
        fleets =1
        pairs.sort(reverse=True)
        prevTime = (target - pairs[0][0]) / pairs[0][1]
        for i, j in pairs:
            currTime = (target - i) / j
            if currTime > prevTime:
                fleets += 1
                prevTime = currTime
        return fleets


        