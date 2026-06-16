class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        for s in strs:
            temp = "".join(sorted(s))
            if temp not in freq:
                freq[temp] = []
            freq[temp].append(s) 

        l = list()
        for t in freq:
            l.append(freq[t])
        return l