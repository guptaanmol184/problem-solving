#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
# https://leetcode.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (30.84%)
# Likes:    10854
# Dislikes: 940
# Total Accepted:    1.5M
# Total Submissions: 4.9M
# Testcase Example:  '[2,1,3]'
#
# Given the root of a binary tree, determine if it is a valid binary search
# tree (BST).
# 
# A valid BST is defined as follows:
# 
# 
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
# 
# 
# 
# Example 1:
# 
# 
# Input: root = [2,1,3]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 10^4].
# -2^31 <= Node.val <= 2^31 - 1
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.innerIsValidBST(root)[0]

    def innerIsValidBST(self, root: Optional[TreeNode]) -> tuple[bool, int, int]:
        root_greater_than_left, root_lesser_than_right, left_valid_bst, right_valid_bst = [True] * 4
        max_left, max_right, min_left, min_right = -math.inf, -math.inf, math.inf, math.inf
        if root.left:
            left_valid_bst, max_left, min_left = self.innerIsValidBST(root.left)
            root_greater_than_left = root.val > max_left
        if root.right:
            right_valid_bst, max_right, min_right = self.innerIsValidBST(root.right)
            root_lesser_than_right = root.val < min_right
        
        maxx = max(max_left, root.val, max_right)
        minn = min(min_left, root.val, min_right)
        
        print(root.val, root_greater_than_left, root_lesser_than_right, left_valid_bst, right_valid_bst)
        return (root_greater_than_left and root_lesser_than_right and left_valid_bst and right_valid_bst, maxx, minn)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validBST(root, left, right):
            if not root:
                return True
            
            if not (left < root.val < right):
                return False
            
            return (validBST(root.left, left, root.val) and
                    validBST(root.left, root.val, right))
        
        return validBST(root, -math.inf, math.inf)


        
# @lc code=end

