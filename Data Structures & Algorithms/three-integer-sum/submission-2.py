class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = list()
        nums = sorted(nums)
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i - 1]:
                continue
            low = i + 1
            high = len(nums) - 1
            
            while low < high:
                if nums[low]+nums[high] +nums[i] == 0:
                    res.append([nums[low], nums[high], nums[i]])

                    low+=1
                    high-=1

                    while low < high and nums[low] == nums[low - 1]:
                        low+=1
                    while low < high and nums[high] == nums[high + 1]:
                        high-=1

                elif nums[low]+nums[high]+nums[i] < 0:
                    low+=1
                else:
                    high-=1
        return res
