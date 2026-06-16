class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        # removed non - alpha chars
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                new_s += s[i]
        # converted all to standard one lower case
        new_s = new_s.lower() 

        low = 0
        high = len(new_s) - 1

        while low < high:
            if new_s[low] != new_s[high]:
                return False
            low+=1
            high-=1
        return True