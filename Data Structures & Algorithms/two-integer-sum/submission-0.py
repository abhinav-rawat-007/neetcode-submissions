class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i , num in enumerate(nums):
            x = target - num
            if x in dict:
                return [dict[x],i]
            dict[num] = i
        