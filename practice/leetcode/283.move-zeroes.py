#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
# https://leetcode.com/problems/move-zeroes/description/
#
# algorithms
# Easy (60.93%)
# Likes:    9852
# Dislikes: 254
# Total Accepted:    1.8M
# Total Submissions: 2.9M
# Testcase Example:  '[0,1,0,3,12]'
#
# Given an integer array nums, move all 0's to the end of it while maintaining
# the relative order of the non-zero elements.
# 
# Note that you must do this in-place without making a copy of the array.
# 
# 
# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:
# Input: nums = [0]
# Output: [0]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# -2^31 <= nums[i] <= 2^31 - 1
# 
# 
# 
# Follow up: Could you minimize the total number of operations done?
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_ptr = -1
        for i in range(len(nums)):
            if nums[i] != 0:
                num_ptr += 1
                temp = nums[i]
                nums[i] = nums[num_ptr]
                nums[num_ptr] = temp
        
# @lc code=end

