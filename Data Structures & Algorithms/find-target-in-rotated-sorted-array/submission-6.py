class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target == nums[0]:
            return 0

        if len(nums) == 2:
            if target == nums[1]:
                return 1
            else:
                return -1
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            
            # if target < nums[left]:
            #     left = mid
            # else:
            #     if target < nums[mid]:
            #         right = mid - 1
            #     else:
            #         left = mid + 1

            #--------
            # left sorted portion
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid
            else: # right sorted part
                if target < nums[mid] or target > nums[right]:
                    right = mid 
                else:
                    left = mid + 1
            
        return -1


