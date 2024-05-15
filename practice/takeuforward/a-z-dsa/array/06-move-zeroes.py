# LC: 283
# https://leetcode.com/problems/move-zeroes/

# TC: O(n) + O(n) = O(n)
# SC: O(1)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        j = -1
        for i in range(0, n):
            if nums[i] == 0:
                continue
            else:
                j +=1 
                nums[j] = nums[i]
        
        for i in range(j+1, n):
            nums[i] = 0
        
        return nums

# TC: O(n)
# SC: O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        j = -1
        for i in range(0, n):
            if nums[i] == 0:
                continue
            else:
                j +=1 
                # swap
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
        
        return nums