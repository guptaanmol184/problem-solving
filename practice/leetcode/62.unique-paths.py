#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#
# https://leetcode.com/problems/unique-paths/description/
#
# algorithms
# Medium (60.64%)
# Likes:    10185
# Dislikes: 319
# Total Accepted:    1M
# Total Submissions: 1.7M
# Testcase Example:  '3\n7'
#
# There is a robot on an m x n grid. The robot is initially located at the
# top-left corner (i.e., grid[0][0]). The robot tries to move to the
# bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move
# either down or right at any point in time.
# 
# Given the two integers m and n, return the number of possible unique paths
# that the robot can take to reach the bottom-right corner.
# 
# The test cases are generated so that the answer will be less than or equal to
# 2 * 10^9.
# 
# 
# Example 1:
# 
# 
# Input: m = 3, n = 7
# Output: 28
# 
# 
# Example 2:
# 
# 
# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach
# the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
# 
# 
# 
# Constraints:
# 
# 
# 1 <= m, n <= 100
# 
# 
#

# @lc code=start
class Solution:
    # Brute Force with TLE
    def uniquePaths(self, m: int, n: int) -> int:
        def unique_paths_internal(cur, end, res):
            if cur == end:
                res[0] += 1
            else:
                curx, cury = cur
                # move right
                if cury <= end[1]:
                    unique_paths_internal((curx, cury + 1), end, res)
                # move down
                if curx <= end[0]:
                    unique_paths_internal((curx + 1, cury), end, res)
        
        res = [0]
        unique_paths_internal((0, 0), (m-1, n-1), res)

        return res[0]  

    # Using Math and combinatorics
    # For every path, we need to move m-1 moves down and n-1 moves to the right.
    # Hence every path needs a total of m + n - 2 moves.
    # The number of unique paths can be determined by finding the number of
    # combinations (ie. ways of choose m - 1 paths for down from m + n - 2 objects)
    # Or (choosing n - 1 paths for right from m + n - 2 objects)
    # ie. (m + n - 2) C (m - 1)
    # T: O(1)
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(m + n - 2, m - 1)
    
        
# @lc code=end

