class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for i , num in enumerate(nums):
            if num in dict:
                return True
            dict[num] = i + 1
        return False  

        