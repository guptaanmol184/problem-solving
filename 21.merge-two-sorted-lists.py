#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (60.93%)
# Likes:    13398
# Dislikes: 1214
# Total Accepted:    2.4M
# Total Submissions: 3.9M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# You are given the heads of two sorted linked lists list1 and list2.
# 
# Merge the two lists in a one sorted list. The list should be made by splicing
# together the nodes of the first two lists.
# 
# Return the head of the merged linked list.
# 
# 
# Example 1:
# 
# 
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# 
# 
# Example 2:
# 
# 
# Input: list1 = [], list2 = []
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: list1 = [], list2 = [0]
# Output: [0]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list1_ptr, list2_ptr = list1, list2

        head = None
        if list1_ptr.val < list2_ptr.val:
            head = list1_ptr
            list1_ptr = list1_ptr.next
        else:
            head = list2_ptr
            list2_ptr = list2_ptr.next
        
        last = head
        while list1_ptr != None and list2_ptr != None:
            if list1_ptr.val < list2_ptr.val:
                last.next = list1_ptr
                last = list1_ptr
                list1_ptr = list1_ptr.next
            else:
                last.next = list2_ptr
                last = list2_ptr
                list2_ptr = list2_ptr.next
            
        non_empty_ptr = list1_ptr if list1_ptr != None else list2_ptr
        last.next = non_empty_ptr # rest not needed to be set, since automatically set in the LL
    
        return head

        
# @lc code=end

