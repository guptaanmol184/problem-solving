#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#
# https://leetcode.com/problems/contains-duplicate/description/
#
# algorithms
# Easy (61.05%)
# Likes:    5582
# Dislikes: 980
# Total Accepted:    1.8M
# Total Submissions: 3M
# Testcase Example:  '[1,2,3,1]'
#
# Given an integer array nums, return true if any value appears at least twice
# in the array, and return false if every element is distinct.
# 
# 
# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    # Using a hash map
    # T: O(n) | S: O(n)
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_tracked = set()
        for num in nums:
            if num in num_tracked:
                return True
            else:
                num_tracked.add(num)
        
        return False
        
# @lc code=end

