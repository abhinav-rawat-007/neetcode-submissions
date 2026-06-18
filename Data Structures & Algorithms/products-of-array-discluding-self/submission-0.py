class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]: 
        left = []
        right = []
        prefix = 1

        for n in nums:
            left.append(prefix)
            prefix*=n
        
        suffix = 1
        for n in reversed(nums):
            right.append(suffix)
            suffix*=n
        
        right = right[::-1]
        
        result = []

        for l , r in zip(left,right):
            result.append(l*r)
        
        return result
              


            
        