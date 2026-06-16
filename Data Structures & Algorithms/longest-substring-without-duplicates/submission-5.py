class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        freq = {}
        count = 0
        while right<len(s):
            if s[right] in freq and freq[s[right]] >= left:
                left= freq[s[right]] + 1
           
            freq[s[right]] = right
            count = max(count , right - left + 1)
            right+=1
        return count
        