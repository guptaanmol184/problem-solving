## Freshworks Practice

import math

# Valid BST

def isBST(node):
    isBSTUtil(node, -math.inf, math.inf)
    

def isBSTUtil(node, mini, maxi):
    if node is None:
        return True
    
    if node.data < mini or node.data > maxi:
        return False
    
    return isBSTUtil(node.left, mini, node.data - 1) and isBSTUtil(node.right, node.data + 1, maxi)

## Using Inorder Traversal
# Traverse the tree ans store is an array, the output should be sorted
# Traverse the tree and check if the oupput follows ascending order


# Cycle in linked list

## Hashing

def hasCycle(head):
    if not head:
        return False
    
    s = set()

    while head:
        if head in s:
            return True
        
        s.add(head)
        head = head.next
    
    return False

## Slow Fast
        
def hasCycle(head):
    if not head:
        return False
    
    slow, fast = head, head

    while fast and fast.next:
        
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    
    return False

# Linked List intersection

# O(n^2)
# Mark Visited nodes - modification of the linked list, extra space
# Hash storage - no modification, but extra space

# Using difference in node counts
#   Count nodes in both the linked lists -  c, d
#   Get the abs(c-d) = e
#   Trverse the big linked list to e nodes
#   Now they have same length, so traverse them parallely to get the first common node
#   Node, check should be on addresses - values can be same, but addresses need not

# Mid element of linked list

# Traverse the linked list, count the nodes, traverse the ll again till count // 2
# Slow and fast pointer. When fast pointer reaches end of ll, slow pointer will be in the middle.

# Perfect Cube

## Check numbers from 1 to n to see if the number is a perfect cube.
## Use inbuild function to find floor of cube root, the check if product is equal to n.
## Find all prime factors, store the frequency of all prime factors in a hash map, if anyone is not 3, return false.

# Finding all primes
## Keep factoring by 2
## Then keep factoring by 3 to sqrt(n), with increment of 2

# Construct a binary tree from post order and pre order traversal
## 

# Kth smallest element in an array
## Sort, index k-1
## Create min heap, call extract min k times
## Create max heap from first k, if new element is smaller than the max insert it and remove the root, else ignore. Return the root.
##  TC: O(k + (N-k) * Log K)
##  S: O(k)
## Quick Partition | Quick Select to partition the array. If index is k, return
##  TC: O(n^2), Avg: O(n)
##  S: O(1)
# Using map and fequency

# Three sum