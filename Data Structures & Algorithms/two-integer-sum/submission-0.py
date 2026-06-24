class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}

        for i, n in enumerate(nums):
            temp = target - n
            if temp in freq:
                return [freq[temp], i]
            freq[n] = i
        return []