class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1 or k == 1:
            return nums
        if k == len(nums):
            return [max(nums)]
        l = 0
        r = 0
        maxList = list()
        for r in range( len(nums)-k+1):
            maxList.append(max(nums[r : r+k]))
        return maxList