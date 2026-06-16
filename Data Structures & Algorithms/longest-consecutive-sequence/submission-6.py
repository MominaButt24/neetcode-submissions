class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        nums = set(nums) 
        nums = list(sorted(nums))
        max_seq = float('-inf')
        count = 1
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                count = count + 1
                if count > max_seq:
                    max_seq = count
            else:
                count = 1
        
        if max_seq < 0:
            return count
        return max_seq
