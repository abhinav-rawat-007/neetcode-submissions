class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        n = len(nums)
        res = []
        while i < n:
            j = i + 1
            k = n - 1
            target = -nums[i]
            if nums[i] == nums[i-1] and i > 0:
                i += 1
                continue
            while j < k:
                if(target == nums[j] + nums[k]):
                    res.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while(j > 0 and j < k and nums[j] == nums[j-1] ):
                        j+=1
            
                    while(k < n-1 and j < k and nums[k] == nums[k+1]):
                        k-=1
                    
                elif target > nums[j] + nums[k]:
                    j += 1
                
                elif target < nums[j] + nums[k]:
                    k -= 1
            
            i += 1
                       
        return res
                    
        