class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            alive = True
            while stack and stack[-1] >0 and i<0:
                if abs(i) > abs(stack[-1]):
                    stack.pop()
                elif abs(i) == abs(stack[-1]):
                    stack.pop()
                    alive = False
                    break
                else:
                    alive = False
                    break
            if alive:
                stack.append(i)
            
        return stack