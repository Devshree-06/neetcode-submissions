class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        arr = []
        for i ,n in enumerate(nums):
            p = target - n
            if p in lookup:
                return [lookup[p],i]
            lookup[n] = i
                

        