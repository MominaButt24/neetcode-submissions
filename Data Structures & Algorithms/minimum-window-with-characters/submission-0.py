class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        freq = {}
        for i in range(len(t)):
            freq[t[i]] = freq.get(t[i], 0) + 1

        l = 0
        minLen = float('inf')
        start = -1
        count = 0
        for r in range(len(s)):
            if s[r] in freq:
                if freq[s[r]] > 0:
                    count +=1
                freq[s[r]]-=1
            while count == len(t):
                if minLen > (r - l + 1):
                    minLen = r - l + 1
                    start = l

                if s[l] in freq:
                    freq[s[l]]+=1
                    if freq[s[l]] > 0:
                        count-=1
                l+=1
        if start == -1:
            return ""
        return s[start : start+minLen]