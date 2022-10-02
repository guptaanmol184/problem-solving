#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (71.09%)
# Likes:    13111
# Dislikes: 227
# Total Accepted:    2.3M
# Total Submissions: 3.2M
# Testcase Example:  '[1,2,3,4,5]'
#
# Given the head of a singly linked list, reverse the list, and return the
# reversed list.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# 
# 
# Example 2:
# 
# 
# Input: head = [1,2]
# Output: [2,1]
# 
# 
# Example 3:
# 
# 
# Input: head = []
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
# 
# 
# 
# Follow up: A linked list can be reversed either iteratively or recursively.
# Could you implement both?
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Iterative. Use two variables. Prev and current. use a temp variable to remove the next before breaking the link.
    # T: O(n) | S: O(1)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        prev = head
        curr = head.next
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head.next = None

    # Recursive approach
    # Keeping two values in memory, recursively keeping them so that you can remember the prev and current even when breaking the link.
    # T: O(n) | S: O(n) - recursion
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        new_head = self.reverseListRecur(head)
        head.next = None
        return new_head
        
        
    def reverseListRecur(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        curr = head.next

        if curr is None:
            return prev
        else:
            head = self.reverseList(curr)
            curr.next = prev
            return head
        
# @lc code=end

