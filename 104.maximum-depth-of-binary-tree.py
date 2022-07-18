#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (72.36%)
# Likes:    7681
# Dislikes: 131
# Total Accepted:    1.8M
# Total Submissions: 2.5M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given the root of a binary tree, return its maximum depth.
# 
# A binary tree's maximum depth is the number of nodes along the longest path
# from the root node down to the farthest leaf node.
# 
# 
# Example 1:
# 
# 
# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# 
# 
# Example 2:
# 
# 
# Input: root = [1,null,2]
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 10^4].
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

    # Recursive: Using stack (DFS)
    # T: O(n) - vising all nodes | S: O(n) - stack 
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    from collections import deque
    # BFS, iterative
    # T: O(n) | S: O(n)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque()
        q.append((root, 1))

        max_depth = 0
        while q:
            node, depth = q.popleft()
            if depth > max_depth:
                max_depth = depth
            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))
            
        return max_depth
    
    # DFS, iterative
    # T: O(n) | S: O(n)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_depth = 0
        stack = [(root, 1)]
        while stack:
            node, depth = stack.pop()
            if depth > max_depth:
                max_depth = depth
            if node.left:
                stack.append((node.left, depth+1))
            if node.right:
                stack.append((node.right, depth+1))
        
        return max_depth









        
# @lc code=end

