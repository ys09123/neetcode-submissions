class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        longest = 0

        for i in st:
            if i - 1 not in st:
                l = 1
                while i + l in st:
                    l += 1
                
                longest = max(l, longest)
        
        return longest