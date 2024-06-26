#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
# https://leetcode.com/problems/daily-temperatures/description/
#
# algorithms
# Medium (67.46%)
# Likes:    7673
# Dislikes: 169
# Total Accepted:    432.1K
# Total Submissions: 639.5K
# Testcase Example:  '[73,74,75,71,69,72,76,73]'
#
# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days you have to
# wait after the i^th day to get a warmer temperature. If there is no future
# day for which this is possible, keep answer[i] == 0 instead.
# 
# 
# Example 1:
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:
# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:
# Input: temperatures = [30,60,90]
# Output: [1,1,0]
# 
# 
# Constraints:
# 
# 
# 1 <= temperatures.length <= 10^5
# 30 <= temperatures[i] <= 100
# 
# 
#

# @lc code=start
class Solution:

    # Brute Force
    # T: O(n^2) | S: O(1)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0] * len(temperatures)
        for i in range(len(temperatures)):
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    out[i] = j - i
                    break
        return out

    # Monotonic Stack
    # T: O(n) | S: O(n)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stack_val, stack_index = stack.pop()
                out[stack_index] = i - stack_index
            stack.append((t, i))
        return out


        
# @lc code=end

