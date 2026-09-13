class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, n in enumerate(nums):
            map[n] = i

        for i, n in enumerate(nums):
            req = target - nums[i]
            if req in map and map[req] != i:
                return [i, map[req]]
            
        
        return []