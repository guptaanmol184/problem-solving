#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
#
# algorithms
# Medium (62.50%)
# Likes:    8154
# Dislikes: 2404
# Total Accepted:    1.2M
# Total Submissions: 1.9M
# Testcase Example:  '[7,1,5,3,6,4]'
#
# You are given an integer array prices where prices[i] is the price of a given
# stock on the i^th day.
# 
# On each day, you may decide to buy and/or sell the stock. You can only hold
# at most one share of the stock at any time. However, you can buy it then
# immediately sell it on the same day.
# 
# Find and return the maximum profit you can achieve.
# 
# 
# Example 1:
# 
# 
# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit =
# 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 =
# 3.
# Total profit is 4 + 3 = 7.
# 
# 
# Example 2:
# 
# 
# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit =
# 5-1 = 4.
# Total profit is 4.
# 
# 
# Example 3:
# 
# 
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: There is no way to make a positive profit, so we never buy the
# stock to achieve the maximum profit of 0.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= prices.length <= 3 * 10^4
# 0 <= prices[i] <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    # Brute force using recursion
    # T: O(n^n) | S: O(n) -> Recursion
    def maxProfit(self, prices: List[int]) -> int:
        return self.maxProfitWithBuyOnIndex(prices, 0)

    def maxProfitWithBuyOnIndex(self, prices: List[int], index: int) -> int:
        # Base case
        if index >= len(prices):
            return 0

        maximum = 0
        for start in range(index, len(prices)):
            max_profit = 0
            for end in range(start + 1, len(prices)):
                if prices[end] > prices[start]:
                    profit = self.maxProfitWithBuyOnIndex(prices, end + 1) + prices[end] - prices[start]
                    if profit > max_profit:
                        max_profit = profit
            if max_profit > maximum:
                maximum = max_profit
        
        return maximum

    # Valleys and Peaks
    # T: O(n) | S: O(1)
    def maxProfit(self, prices: List[int]) -> int:
        valley = prices[0]
        peak = 0
        profit = 0

        i = 1
        while i < len(prices):
            while i < len(prices) and prices[i] < prices[i-1]:
                valley = prices[i]
                i += 1
            
            while i < len(prices) and  prices[i] >= prices[i-1]:
                peak = prices[i]
                i += 1
            
            if peak != 0:
                profit += peak - valley

            peak = 0
    
        return profit

    # Single one pass
    # T: O(n) | S: O(1)
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i] <= prices[i+1]:
                profit += prices[i+1] - prices[i]
        
        return profit

        

# @lc code=end

