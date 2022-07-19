#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#
# https://leetcode.com/problems/diameter-of-binary-tree/description/
#
# algorithms
# Easy (54.92%)
# Likes:    8667
# Dislikes: 537
# Total Accepted:    801K
# Total Submissions: 1.5M
# Testcase Example:  '[1,2,3,4,5]'
#
# Given the root of a binary tree, return the length of the diameter of the
# tree.
# 
# The diameter of a binary tree is the length of the longest path between any
# two nodes in a tree. This path may or may not pass through the root.
# 
# The length of a path between two nodes is represented by the number of edges
# between them.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
# 
# 
# Example 2:
# 
# 
# Input: root = [1,2]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 10^4].
# -100 <= Node.val <= 100
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dia = [0]
        def dfs(root):
            if not root:
                return -1
            
            left_h = dfs(root.left)
            right_h = dfs(root.right)

            # diameter
            dia[0] = max(dia[0], left_h + right_h + 2) 
            return 1 + max(left_h, right_h)
        
        dfs(root)
        return dia[0]



        
# @lc code=end

