#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#
# https://leetcode.com/problems/same-tree/description/
#
# algorithms
# Easy (55.83%)
# Likes:    6386
# Dislikes: 144
# Total Accepted:    1.1M
# Total Submissions: 2M
# Testcase Example:  '[1,2,3]\n[1,2,3]'
#
# Given the roots of two binary trees p and q, write a function to check if
# they are the same or not.
# 
# Two binary trees are considered the same if they are structurally identical,
# and the nodes have the same value.
# 
# 
# Example 1:
# 
# 
# Input: p = [1,2,3], q = [1,2,3]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: p = [1,2], q = [1,null,2]
# Output: false
# 
# 
# Example 3:
# 
# 
# Input: p = [1,2,1], q = [1,1,2]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in both trees is in the range [0, 100].
# -10^4 <= Node.val <= 10^4
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
    # Recursive
    # T: O(n) | S: O(n) - stack
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            return p is None and q is None
        
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

    
    # Iterative DFS
    # T: O(n) | S: O(n)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        while stack:
            node1, node2 = stack.pop()
            if not node1 and not node2:
                continue
            elif None in [node1, node2]:
                return False
            else:
                if node1.val != node2.val:
                    return False
                else:
                    stack.append((node1.right, node2.right))
                    stack.append((node1.left, node2.left))
        return True


        
# @lc code=end

