#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (31.52%)
# Likes:    19353
# Dislikes: 1850
# Total Accepted:    2.1M
# Total Submissions: 6.6M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an integer array nums, return all the triplets [nums[i], nums[j],
# nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] +
# nums[k] == 0.
# 
# Notice that the solution set must not contain duplicate triplets.
# 
# 
# Example 1:
# 
# 
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[1] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not
# matter.
# 
# 
# Example 2:
# 
# 
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# 
# 
# Example 3:
# 
# 
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
# 
# 
# 
# Constraints:
# 
# 
# 3 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution:

    # Sorting + Using 2 pointers
    # T: O(nlogn) + O(n^2) = O(n^2) | S: O(1)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, val in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            target = -val

            l_ptr = i+1
            r_ptr = len(nums) - 1

            while l_ptr < r_ptr:
                current_sum = nums[l_ptr] + nums[r_ptr]

                if current_sum < target:
                    l_ptr += 1
                elif current_sum > target:
                    r_ptr -= 1
                else:
                    res.append([val, nums[l_ptr], nums[r_ptr]])
                    l_ptr += 1
                    while nums[l_ptr] == nums[l_ptr - 1] and l_ptr < r_ptr:
                        l_ptr +=1
        
        return res

        
# @lc code=end

