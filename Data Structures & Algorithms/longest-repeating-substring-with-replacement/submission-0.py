class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = 0
        maxFreq = 0
        freq = {}

        for right in range(len(s)):
            
                
            freq[s[right]] = freq.get(s[right], 0) + 1
            maxFreq = max(maxFreq, freq[s[right]])
            if (right-left+1) - maxFreq > k:
                freq[s[left]]-=1
                left+=1
            elif (right-left+1) - maxFreq <= k:
                
                count = max(count, right - left + 1)
        return count
            