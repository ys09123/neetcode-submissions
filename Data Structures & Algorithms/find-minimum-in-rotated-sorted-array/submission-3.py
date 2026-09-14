class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        h = len(nums) - 1

        while l <= h:
            m = l + (h - l) // 2
            if nums[l] <= nums[h]:
                return nums[l]
            if nums[m] > nums[h]:
                l = m + 1
            else:
                h = m
        
        return 0