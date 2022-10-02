#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
#
# algorithms
# Medium (59.72%)
# Likes:    6944
# Dislikes: 1024
# Total Accepted:    1.1M
# Total Submissions: 1.9M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given a 1-indexed array of integers numbers that is already sorted in
# non-decreasing order, find two numbers such that they add up to a specific
# target number. Let these two numbers be numbers[index1] and numbers[index2]
# where 1 <= index1 < index2 <= numbers.length.
# 
# Return the indices of the two numbers, index1 and index2, added by one as an
# integer array [index1, index2] of length 2.
# 
# The tests are generated such that there is exactly one solution. You may not
# use the same element twice.
# 
# Your solution must use only constant extra space.
# 
# 
# Example 1:
# 
# 
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We
# return [1, 2].
# 
# 
# Example 2:
# 
# 
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We
# return [1, 3].
# 
# 
# Example 3:
# 
# 
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We
# return [1, 2].
# 
# 
# 
# Constraints:
# 
# 
# 2 <= numbers.length <= 3 * 10^4
# -1000 <= numbers[i] <= 1000
# numbers is sorted in non-decreasing order.
# -1000 <= target <= 1000
# The tests are generated such that there is exactly one solution.
# 
# 
#

# @lc code=start
class Solution:

    # Binary search
    # T: O(nlogn) | S: O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i in range(len(numbers)):
            num1 = numbers[i]
            num2 = target - num1

            index = self.bin_search(numbers, 0, len(numbers) - 1, num2)
            if index != -1:
                return [i + 1, index + 1]

    
    def bin_search(self, numbers, start, end, search_num):
        if end > start:
            return -1

        mid = start + (end - start) // 2
        if numbers[mid] == search_num:
            return mid
        elif numbers[mid] > search_num:
            self.bin_search(numbers, start, mid-1, search_num)
        else:
            self.bin_search(numbers, mid+1, end, search_num)

    # Two pointers
    # T: O(n) | S: O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l_ptr = 0
        r_ptr = len(numbers) - 1

        while (l_ptr < r_ptr):
            current_sum = numbers[l_ptr] + numbers[r_ptr]
            if current_sum == target:
                return [l_ptr + 1, r_ptr + 1]
            elif current_sum < target:
                l_ptr += 1
            else:
                r_ptr += 1
        
# @lc code=end

