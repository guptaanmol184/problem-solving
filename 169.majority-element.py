#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (63.33%)
# Likes:    10612
# Dislikes: 357
# Total Accepted:    1.3M
# Total Submissions: 2.1M
# Testcase Example:  '[3,2,3]'
#
# Given an array nums of size n, return the majority element.
# 
# The majority element is the element that appears more than ⌊n / 2⌋ times. You
# may assume that the majority element always exists in the array.
# 
# 
# Example 1:
# Input: nums = [3,2,3]
# Output: 3
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
# 
# 
# Constraints:
# 
# 
# n == nums.length
# 1 <= n <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9
# 
# 
# 
# Follow-up: Could you solve the problem in linear time and in O(1) space?
#

import collections

# @lc code=start
class Solution:
    # Using python Counter
    # T: O(n) | O(n) -> since it's keep a count of the objects
    def majorityElement(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        return c.most_common(1)

    # Using Boyer Moore Voting Algorithm
    # T: O(n) | O(n) -> since it's keep a count of the objects
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        return candidate

        
# @lc code=end

