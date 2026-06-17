class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1 or k == 1:
            return nums
        if k == len(nums):
            return [max(nums)]
        # ---- less efficient - time exceed -----
        # r = 0
        # maxList = list()
        # for r in range( len(nums)-k+1):
        #     maxList.append(max(nums[r : r+k]))
        # return maxList
        # ---- more efficeint ----
        q = deque()
        maxList = list()
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                maxList.append(nums[q[0]])
                l += 1
            r += 1

        return maxList