class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freq1 = {}
        freq2 = {}
        s1 = ''.join(sorted(s1))
         
        for r in range(len(s2)):
            if s1 == ''.join(sorted(s2[r:r+len(s1)])):
                return True
        return False
        # l = 0
        # count = 0
        # for r in range(len(s2)):
        #     if s2[r] not in freq:
        #         if s2[l] in freq:
        #             freq[s2[l]] +=1
        #         l = r + 1
        #     elif freq[s2[r]] == 0:
        #         freq[s2[l]] +=1
        #         l += 1
        #     else:
        #         freq[s2[r]] -= 1
        #         count = max(count, r - l + 1)
        # return count == len(s1)
