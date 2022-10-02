#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
# https://leetcode.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (66.03%)
# Likes:    6455
# Dislikes: 225
# Total Accepted:    862.8K
# Total Submissions: 1.3M
# Testcase Example:  '5'
#
# Given an integer numRows, return the first numRows of Pascal's triangle.
# 
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it as shown:
# 
# 
# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:
# Input: numRows = 1
# Output: [[1]]
# 
# 
# Constraints:
# 
# 
# 1 <= numRows <= 30
# 
# 
#

# @lc code=start
class Solution:
    # Generate the triangle step by step
    # T: O(n^2) | S: O(n^2)
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        result.append([1])

        for i in range(1, numRows):
            last_row = result[-1]

            new_row = []
            new_row.append(1)
            for i in range(1, len(last_row)):
                new_row.append(last_row[i] + last_row[i-1])
            new_row.append(1)
            
            result.append(new_row)
        
        return result


        
# @lc code=end

