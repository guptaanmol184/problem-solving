# LC: 26
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

def removeDuplicates(self, nums: List[int]) -> int:
    l = 0
    r = 1
    
    while r < len(nums):
        if nums[l] != nums[r]:
            l += 1
            nums[l] = nums[r]
        r += 1
    
    return l + 1

# Learning:
# Think of the clear base case and build your solution from there, do not try to tackle the complete problem.
# You need to define starting state and build