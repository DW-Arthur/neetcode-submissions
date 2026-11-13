class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # For the sliding window
        # I need to have a window count and max frequnecy
        # Hashmap for the counts for each character, the window count is the totoal count
        # The formula
        # windowSize - maxFreq, get the max change of the array, once the max has been found
        # Then add it to the count of the selected maxFreq, then that should be the result
        # Shrink the left pointer if windowSize - maxFreq > k, keep going until right pointer reaches the end
        # X = 1
        # windowSize =1, maxFreq = 1, diff =1
        # X =1, Y =1
        # windowSize = 2, maxFreq = 1, diff = 1 
        # X =1, Y =2
        # windowSize = 3, maxFreq = 2, diff = 1
        # X = 2, Y = 2
        # WindowSize =4, maxFreq = 2, diff = 2
        # Return the max windowSize that is less than k
        left = 0
        res = 0
        maxFreq = 0
        freq = {}

        for right in range(len(s)):
            # 1. Add incoming character s[right] to hashmap
            freq[s[right]] = freq.get(s[right], 0) + 1
            
            # 2. Update the highest frequency seen in the current window
            maxFreq = max(maxFreq, freq[s[right]])

            # 3. Shrink from the left while the CURRENT window is invalid
            while (right - left + 1) - maxFreq > k:
                freq[s[left]] -= 1
                left += 1

            # 4. Current window is now valid; record the max length
            res = max(res, right - left + 1)

        return res

        