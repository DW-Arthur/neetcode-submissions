class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Maybe sort the array first
        # Have 2 pointers that constantly try to find the limit
        # Try to fit the heavist person to the boat first, fill 2 if possible
        people.sort()
        left, right =0, len(people)-1
        result = 0
        while left <= right:
            if people[left] + people[right] > limit:
                result +=1
                right -=1
                continue
            if people[left] + people[right] <= limit:
                result +=1
                left +=1
                right -=1
        return result
        