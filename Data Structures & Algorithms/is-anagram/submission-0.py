class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        if len(s) != len(t):
            return False
        chars = {}
        for i in s:
            chars[i] = chars.get(i, 0) + 1
        for i in t:
            if i in chars and chars[i] > 0:
                chars[i]-=1
            else:
                return False
        return True