class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Find the time it takes for the cars to reach the end
        # Compare the two, the smaller time means it reaches first, so it will collide with
        # the first car
        # formula is (target - position)/speed
        # Sort the array based on position forst
        # Have a hashmap that o
        # Add position and speed together
        array = []
        for i in range(len(position)):
            array.append([position[i], speed[i]])
        array.sort()
        # Iterate from the last spot?
        stack =[]
        result = 0
        for i in range(len(array)-1, -1, -1):
            time = (target-array[i][0])/array[i][1]
            while stack and time > stack[-1]:
                stack.pop()
            if len(stack) ==0:
                result +=1
            stack.append(time)
        return result
