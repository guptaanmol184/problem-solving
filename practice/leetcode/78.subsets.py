#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (72.36%)
# Likes:    11066
# Dislikes: 167
# Total Accepted:    1.2M
# Total Submissions: 1.6M
# Testcase Example:  '[1,2,3]'
#
# Given an integer array nums of unique elements, return all possible subsets
# (the power set).
# 
# The solution set must not contain duplicate subsets. Return the solution in
# any order.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# 
# 
# Example 2:
# 
# 
# Input: nums = [0]
# Output: [[],[0]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.
# 
# 
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def list_subsets(i: int, nums: List[int], B: List[int], res: List[List[int]]):
            if index == len(nums):
                sol = []
                for index, ele in enumerate(B):
                    if ele == 1:
                        sol.append(nums[index])
                res.append(sol)
            else:
                B[i] = 1
                list_subsets(i+1, nums, B, res)

                B[i] = 0
                list_subsets(i+1, nums, B, res)
        
        res = []
        B = [0] * len(nums)
        list_subsets(0, nums, B, res)

        return res
        
        # neetcode
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return res

# @lc code=end

