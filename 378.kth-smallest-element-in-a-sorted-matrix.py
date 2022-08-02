#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
#
# algorithms
# Medium (60.02%)
# Likes:    6549
# Dislikes: 249
# Total Accepted:    417K
# Total Submissions: 691.3K
# Testcase Example:  '[[1,5,9],[10,11,13],[12,13,15]]\n8'
#
# Given an n x n matrix where each of the rows and columns is sorted in
# ascending order, return the k^th smallest element in the matrix.
# 
# Note that it is the k^th smallest element in the sorted order, not the k^th
# distinct element.
# 
# You must find a solution with a memory complexity better than O(n^2).
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
# Output: 13
# Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and
# the 8^th smallest number is 13
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[-5]], k = 1
# Output: -5
# 
# 
# 
# Constraints:
# 
# 
# n == matrix.length == matrix[i].length
# 1 <= n <= 300
# -10^9 <= matrix[i][j] <= 10^9
# All the rows and columns of matrix are guaranteed to be sorted in
# non-decreasing order.
# 1 <= k <= n^2
# 
# 
# 
# Follow up:
# 
# 
# Could you solve the problem with a constant memory (i.e., O(1) memory
# complexity)?
# Could you solve the problem in O(n) time complexity? The solution may be too
# advanced for an interview but you may find reading this paper fun.
# 
# 
#

# @lc code=start
import heapq
class Solution:
    # Using heap
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or not matrix[0]:
            return -1
        heap = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                nextVal = -matrix[row][col]
                if len(heap) < k:
                    heapq.heappush(heap, nextVal)
                elif nextVal > heap[0]:
                    heapq.heappushpop(heap, nextVal)
        return -heap[0]
        
# @lc code=end

