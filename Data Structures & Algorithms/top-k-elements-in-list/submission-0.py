class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        l = sorted(freq.items(), key=lambda item: item[1], reverse=True)
        ans = list()
        for i in range(k):
            key , val = l[i]
            ans.append(key)
        return ans

    

