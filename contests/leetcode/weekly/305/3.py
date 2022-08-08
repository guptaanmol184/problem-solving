from typing import *
import sys
sys.setrecursionlimit(550000)

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        @cache
        def partition(i):
            if i == len(nums):
                return True

            # apply 1
            res = False
            if n > i + 1 and nums[i] == nums[i+1]:
                if partition(i+2):
                    return True
            
            # apply 2
            if n > i + 2 and nums[i] == nums[i+1] == nums[i+2]:
                if partition(i+3):
                    return True
            
            # apply 3
            if n > i + 2 and nums[i+2] == nums[i+1] + 1 == nums[i] + 2:
                if partition(i+3):
                    return True
            
            return res 
        
        return partition(0)
        
s = Solution() 
out = s.validPartition([4,4,4,5,6])
print(out)
out = s.validPartition([1,1,1,2])
print(out)
