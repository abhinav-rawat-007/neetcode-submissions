class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        count_s1 = {}
        count_s2 = {}
        for s in range(len(s1)):
            count_s1[s1[s]] = count_s1.get(s1[s], 0) + 1
         
        for right in range(len(s2)):
            count_s2[s2[right]] = count_s2.get(s2[right] ,0) + 1  
            while right-left+1 > len(s1):
                count_s2[s2[left]] -= 1
                if count_s2[s2[left]] == 0:
                    del count_s2[s2[left]]
                left+=1

            if count_s1 == count_s2:
                return True
        
        return False

            



        