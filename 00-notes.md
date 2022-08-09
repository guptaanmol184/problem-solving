# Problem solving notes

## 1. Two sum
P: Find if a given array contains pair of numbers with a target sum. Pair is guaranteed to exist.

S:
1. Look using 2 for loops through all pairs.
2. Verify if they sum to the target sum value.
T: O(N^2) | S: O(1)

S:
1. Use map to store already seen numbers
2. Go through each number and see if complement is already available in map
T: O(N) | O(1)

## 2. Best time to buy and sell stock
P: Given a array of daily prices, find the best time to buy and sell stock to make maximum profit.

S: Brute force
1. Traverse through array using 2 for loops for all pairs
2. Calculate profile and keep updating maximum profit
T: O(n^2) | O(1)

S: Finding highest peak after smallest valley
1. Use 2 variables min_price and max_profit.
    - min_price demotes the minimum price till now.
    - max_profit denotes the maximum profit till now.
2. max_profit is calculated for each variable by assuming the current value as maximum and checking profit with min_price
T: O(n) | O(1)

## 3. Merge Sorted Array
P: Given 2 sorted arrays, 1 length m+n one length n, and m and n. Merge them in place in the m+n so that output is sorted.

S: 3 pointers - nums1_ptr, nums2_ptr, insert_ptr
1. Compare values from nums1 and nums2, pick largest
2. Insert into insert_ptr location at nums1 array
3. Keep doing until nums2 is empty

## 4. Move Zeros (283)
P: Given an array of numbers, move all the zeros to the end of the array while keeping the relative ordering of other numbers as is

S: 2 pointers - num tracking and traversing
1. Traverse through the array
2. If the val at index is not zero, increment the num tracking and swap it with val at the index.
3. If the value at index is zero, proceed to next index.

Coagulates and moves zeros to the end

## 5. Buy and Sell Stock II (122)
P: Given a array of daily prices, find the max profit you can make by buying and selling the stock multiple times.

S: Brute Force
1. Recurse through all the possible combinations of stock that you can get and the profit that you can make using it.
T: O(n^n) | S: O(n) recurse

S: Peaks and valleys
TO make the most profit note that the stock should be purchased on a valley and be sold on the corresponding peak. Note that also that we cannot skip any peak,valley since the cumulative profit will be letter than the multiple profits from each individual valley-peak combo.
1. Keep traversing through the array till all elements are covered.
    1. Keep comparing consecutive elements to fall down until there is a valley/through
    2. Keep climbing consecutive elements, until there is a peak.
    3. Add the profit from the valley-peak combo
2. Return the total profit from the valley-pack combos
T: O(n) | S: O(1)

S: Simple one pass ( Peaks and valley)
Looking at peak and valley approach, in a valley-peak combo,
    total profit = profit from each consecutive profitable pair
Traverse the array, adding up profit from each consecutive pair of profitable trade.
T: O(n) | S: O(1)

## 6. Running sum of 1D Array (1480)
Monday (11/07)
P: Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
S: Traverse the array, picking one number at a time from the nums array. Adding a new element to the running_sums array as sum of the last appended running_sums array value and the nums value at the current index.
T: O(n) | S: O(1) -> can be done in place

## 7. Find Pivot Index (724)
Monday (11/07)
P: Given an array of integers nums, calculate the pivot index of this array.  The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
S: Calculate sum of array once. Keep track of left sum as you traverse through the array. Right sum = Total - leftsum - current_val. Use this to check if right_sum == left_sum.
T: O(n) | S: O(1)

## 8. Majority Element
Tuesday (12/07)
P: Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

S: Hash map approach
T: O(n) | S: O(n)

S: Sorting approach
Sort elements are return the element at ⌊n / 2⌋ index
T: O(nlogn) | S: O(1)

S: Boyer Moore Voting approach
Assume the first element to be the candidate. Count +1 for every reoccurrence of candidate, and -1 for any other number.
If the count reaches 0, throw the prefix. This can be safely done because we whenever we are throwing away we can ensure that we are throwing at most equal number of majority elements as the minority elements.
Finally we will be left with such a suffix that has the real majority element.
This process ensures that the actual (global majority) remains the actual majority element in the suffix after throwing away the prefix.
T: O(n) | S: O(1)

## 9. Fibonacci Number
Wednesday (13/07)
P: Given n, return the nth fibonacci number
S: Use f(n) = f(n-1) + f(n-2) iteratively. f(0) = 0, f(1) = 1

## 977 Squares of a sorted array
Wednesday (13/07)
P: Given an array sorted in ascending order, return an array with all elements squared and sorted in ascending order. NOTE: Array may contain negative integers.
S: Note that with negative integers sorted in ascending order. The number with the biggest sqaure will be at the beginning and as we go towards zero sqaure value will reduced. Now, from 0 again squares will increase and towards the end, the sequares will be highest. This let's us use 2 pointers to compare and pick the biggest number to sqaure from the starting and end end. Repeat this shifting the 2 pointers and add it to the result array.
T: O(n) | S(n)

## 118 Pascals Triangle
Wednesday (13/07)
P:Given n, return the first n rows of the pascals triangle
S: Iterate over n, add rows with rows[i][j] = rows[i-1][j] + rows[i-1][j-1]
Note for every row first and last element is 0
Note for every row, we already know the space needed, allocate it at once.
T: O(n^2) | S(n^2)

## 26 Remove Duplicates from Sorted Array
Wednesday (13/07)
P: Given array nums sorted in non-decreeing order. Remove Duplicates in the array in place, keeping the order. Return number of unique elements in the array.
S: 2 pointers, insert_ptr and traverse_ptr
If the current traverse_ptr value is different from it's previous, insert value in insert_ptr location and increment insert_ptr.
T: O(n) | S: O(1)

## 56 Merge Intervals
Thursday (14/07)
P: Given an array of intervals where intervals[i] = [start, end], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
- Find condition for merging two intervals. ie. a, b and c, d merge if c <= b
S: Do this for all elements and make the biggest merges without sorting and update the array
T: O(n^2) | S: O(n)

S: Sort the input using the start elements as keys
For each element check all the other elements and merge.
T: O(n^2) | S: O(n)

S: Sort the input using the start elements as keys
For each consecutive element, merge it with the previous element if merge is possible else, add this as a new element in the output. This uses the face that we have sorted the array using the start elements and overlaps can only be consecutive elements. If, consecutive elements don't overlap, it's a new interval.
T: O(nlogn) | S: O(n)

## 167 Two Sum 2
Friday (15/07)
P: Given a sorted array and a target, find if the array contains the target

S: Refer to Two sum solutions above as they already apply

S: Binary search
Since array is sorted, we can binary search. 
For loop for picking first element.
Use binary search in the rest of array to find the element.
T: O(nlogn) | S: O(1)

S: Two pointers
Since the array is sorted, we can use 2 pointers from starting and end. If the sum is more than expected value, we move the lower end pointer. If the sum is more than expected value, we move the higher end pointer.
T: O(n)| S: O(n)

## 15 3 Sum
Friday (15/07)
P: Given an array and a target, find unique triplets which sum to the given target (eg. 0)
S: Sort the array to know that if you are starting with the same element, then you should skip to avoid duplicates.
For each element considered as the starting element. Check sum needed to get target.
And use 2 sum approach  (ie. 2 pointers) to find the target element in the left over array.
Apply similar logic as starting element duplicate skip for the 2 sum also.
T: O(nlogn) + O(n^2) = O(n^2) | S: O(1)

## 217 Contains Duplicates
Friday (15/07)
P: Given an array, return true if it contains duplicates else return false
S: Brute force
T: O(n^2) | S: O(1)

S: Sorting and traversal
T: O(nlogn) | S: O(1)

S: Hashmap
T: O(n) | S: O(n)

## 242 Valid Anagram
Friday (15/07)
P: Given two strings, return `true` if they are anagrams else `false`
S: Create 2 hash maps to for each string and compare them for ensuring, same length, same character set, and same cont for character
T: O(s+t) | S: O(s+t)

S: Sorting
T: O(nlogn) | S: O(1)

## 125 Valid Palindrome
Friday (15/07)
P: Given a string, check if it's a palindrome. Note only alpha numeric characters should be considered for palindrome check

S: Remove all non alphanumeric chracters. Reverse string. Check.
T: O(n) | S: O(n)

S: 2 pointers
Use 2 pointers for traversing both ends. Use while and bound check loop to skip non alpha num characters.
T: O(n) | S: O(1)

## 20 Valid Parentheses
Friday (15/07)

P: Given a string with only '[', '{', '(', find if it is valid and all parentheses match up

S: Using stack
Use stack to add open parens. On seeing closing paren, verify with top of stack. If success, continue. Else invalid. Valid if stack remains empty in the end.
T: O(n) | S: O(n)

## 704 Binary search
Friday (15/07)
P: Given array sorted in ascending order and a target. Return index if present, else -1.

S: Apply binary search
T: O(logn) | S: O(1)

## 206 Reverse Linked List
Saturday (16/07)
P: Given a linked list, reverse the list.

S: Traverse through the list tracking prev and current nodes. Use a temp variable to store current.next before setting current.next = prev.
Finally set head.next = None
T: O(n) | S: O(1)

S: Recursive approach
Keeping two values in memory, recursively keeping them so that you can remember the prev and current even when breaking the link.
T: O(n) | S: O(n) - recursion

## 21 Mere two sorted lists
Sunday (17/07)
P: Given 2 sorted linked lists merge them.

S: Use 2 pointers, 2 to traverse the individual linked lists, and 1 to keep track of the last element in the merged list, where new elements are added.
- * Use a dummy Node without value for the start, and then return dummy.next - neetcode
T: O(n) | S: O(1)

## 226 Invert Binary Tree
Sunday (17/07)
P: Given a binary tree, invert the nodes

S: Recursive, for each node, invert the children and recursively call invert on the left and right node
T: O(n) | S: O(n) - stack

S: DFS
T: O(n) | S: O(n)

S: BFS
T: O(n) | S: O(n)

## 104 maximum depth of a binary tree
Monday (18/07)
P: Given a binary tree, find it's maximum depth

S: Recursive, dfs, using stack
T: O(n) | S: O(n)

S: BFS using queue
T: O(n) | S: O(n)

S: Iterative DFS using stack
T: O(n) | S: O(n)

## 543 Diameter of binary tree
Monday (18/07)
P: Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.

S: Recursion, DFS:
So, compute the dfs to find the height of the left and right subtrees, while computing also keep looking for diameter. Update max diameter.
1 - None node is height -1, dia = left_h + right_h + 2
2 - None node is height 0, dia = left_h + right_h. Accounts for parents edge, looks simpler.
T: O(n)| S: O(n) - stack

## 110 Balanced Binary Tree
Monday (18/07)
P: Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
    a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

S:
- To calculate the if a tree is balanced we need height of left and right subtrees
- Do DFS and calculate the height of subtrees bottom up, this allows root getting to know it's height and if it's balanced based on subtrees height and balanced.
- Track height and balanced status during the dfs recursively
T: O(n)| S: O(n) -stack

## 100 Same tree
Tuesday (19/07)
P: Given 2 binary tree's. Identify if they are same. Same implies their values and structure are same.

S: DFS and compare nodes.
- Recursive: super easy
- Iterative: Slightly more implementation. Stack comes into picture instead of call stack
T: O(n)| S: O(n)

## 572 Subtree Of Another Tree
Wednesday (20/07)
P: Given a tree and a another tree. Determine if the another tree is a sub tree of the given tree.

S: 
- DFS on the tree, using the above Same Tree to check if the tree is a subtree of the given tree
n - size of tree
m - size of another tree
T: O(n * m)| S: O(n + m) approx space - stack

## 235 Lowest Common Ancestor Of A Binary Search Tree
Thursday (21/07)
P: Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

S:
- Use post order traversal, evaluate if q and p are found in the left and right sub trees. Then evaluate if the value is found in the root.
- Return when value found in the root
T: O(n) | S: O(n)

S: Use BST property and check the current node value with p and q values
T: O(logn) | S: O(1)

## 703 Kth Largest Element In A Stream
Friday (22/07)
P: Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

S:
Using a minheap of size k, since we wan't the kth largest element and only would need to track the k largest elements at any point in the stream

Construction: O(nlogn) because creating heap from array (heapify) is O(n). But, then popping elements until size is k is k * O(logn). ie. total O(nlogn)

Add: Since we are inserting and removing in a min heap. It'll take O(logn) to insert and O(logn) to remove. ie. total: O(logn) + O(logn)

Hence total TC: O(nlong) + O(logn) = O(logn), S: O(k) - storing the k elements in the heap
Use python heapq

## 1041 Robot Bounded In Circle
Sunday (24/07)
P: Given a robot starting at origin and a set of instructions, "G" to go forward, "L" to turn left, "R" to turn right. The robot repeats the instructions in an infinite loop. Find if the robot will forever remain inside a finite radius circle or not ? Return bool.

S: Go through each instruction, based on it update the robot's direction and position. Check if the robot is still at the origin or it's direction is not the starting direction.

## 102 binary tree level order traversal
Sunday (24/07)
P: GIven the root of a binary tree, return the level order traversal of it's node values

S: Do BFS
T: O(n) | S: O(n) - stack space

## 199 Binary Tree Right Side View
Sunday (24/07)
P: Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

S: Do BFS and note down the node in the extreme right
T: O(n) | S: O(n)

## 1448 Count Good nodes in binary tree
Sunday (24/07)
P: Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

S: Do DFS, update the max when moving down the tree and update the global count if the node is a good node.
T: O(n) | S: O(n)

## 2 Add Two Numbers
Sunday (24/07)
P: You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

S: Use 3 pointers, to track the first 2 numbers and the resultant sum. Use s and c variables to keep track of sum and carry in each operation.
T: O(n) | S: O(1) -> s and c

## 98 Validate Binary Search Tree
Monday (25/07)
P: Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

S: Do DFS, tracking the max and min values on the subtree. Use this to deduce if the root is greater than all the left subtree values and root is lesser than all the right subtree values. Recursively check if left and right subtrees are also valid BSTs.
T: O(n) | S: O(logn) or O(n) - stack space, O(n) worst case

Neetcode solution is simpler and easier to understand. It is top down approach for keep track of the bounds the value of the current node should be in.

Backtracking - Generally needs a tracking of the index, bitmask being constructed, the list of nums and the list of results to append the solution to.

## 78 Subsets
Monday (25/07)

P: Given an integer array nums of unique elements, return all possible subsets (the power set).

S: Do DFS, and choose once to include the element and once to not include the element.
T: O(2^n) | S: O(n) - to track the solution in a single list (or) O(2^n) if considering space for answer as well

## 236 Lowest Common Ancestor Of A Binary Tree
Tuesday (26/07)

P: Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

S: Relates to 235, but a binary tree. Do DFS and keep track of p, q being seen on the left and right subtree.
Use this information to identify if the lowest common ancestor has been found if both p and q have been seen.
T: O(n) | S: O(logn) or O(n) in worst case

## 155 Min Stack [S]
Tuesday (26/07)

P: Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

S: Use the constraint that what you are implementing a stack, hence the operations would only be push, pop, top and nothing else and think how can the min be tracked with the operation.

## 150 Evaluate Reverse Polish Notation[S]
Tuesday (26/07)

P: Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

S: Use stack
T: O(n) | S: O(n/2)
*: Learn how to perform division while truncating output to 0. Basically to float division and ignore the value after decimal.

## 114 Flatten Binary Tree To Linked List[S]
Wednesday (27/07)

P: Given the root of a binary tree, flatten the tree into a "linked list". This should be done in pre order traversal.

S: Use a stack for DFS, and add nodes to linked list.
T: O(n) | S: O(logn), worst O(n)

Neetcode has good approach

## 22 Generate Parentheses
Wednesday (27/07)

P: Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

S: Bruteforce - Generate all possible parentheses, then check if they are valid.
T: O(2^n) | S: O(n)

S: Neetcode: Backtrack, using open paren count and closed paren count in the output. Don't follow through for any invalid condition. Once open paren count == closed parent count == n, add to result.
T: ??

## 739 Daily Temperatures [S]
Thursday (28/07)
P: Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

S: Brute Force
T: O(n^2) | S: O(1)

S: Monotonic stack
So, the logic here is that when you see a smaller element you can add it on the top of the stack, since it's not greater. But as you keep on going, when you see a larger element, you keep popping out of the stack all the elements that are smaller than the larger element and update it's value. This helps because, the next greater element is inherently stackish, where one value would be greater for one previous value but not all. And then we remember the current value that's smallest on the top of the stack and look for new values in the array that can pop the current smallest value.

Approach:
- Remembering the index at which we had seen a value
- Calculating the next largest value for all the values on top of the stack that are smaller than the current value (this is possible because a single larger value can be greater for multiple values). This is possible due to remembering the index
- Use stack because if we find a larger value, it may not be the largest for all the values but a subset of values on the top of the stack.
- Keep doing this, and you can find the next largest element for all the elements.

Note: Next smallest element needs a monotonically increasing stack
Note: Next greatest element needs a monotonically decreasing stack
T: O(n) | S: O(n)

## 890 Find And Replace Pattern
Friday (29/07)
P: Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.

S: Use 2 maps to check for bijective mapping.
T: O(p) for each word. | O(p) - 2 dictionaries of size p

## 916 Word Subsets
Saturday (30/07)
P: You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order.

S: Since the universal string should cater to all words in word2. Take the union of the requirements for all word2 words and check with all word1 words to find the solution set.

## 62 Unique Paths [S]
Monday (01/08)
P: Given a m x n matrix, find the number of ways to move from (0, 0) to (m-1, n-1) if only right and down moves are possible.

S: Use combinatorics
T: O(1)

## 853 Car Fleet
Monday (01/08)
P: Read description
S:
Sort cars by the start positions pos
Loop on each car from the end to the beginning
Calculate its time needed to arrive the target
cur records the current biggest time (the slowest)

If another car needs less or equal time than cur,
it can catch up this car fleet.

If another car needs more time,
it will be the new slowest car,
and becomes the new lead of a car fleet.
T: 
O(NlogN) Quick sort the cars by position. (Other sort can be applied)
O(N) One pass for all cars from the end to start (another direction also works).

O(N) Space for sorted cars.
O(1) space is possible if we sort pos inplace.
Best explanation: https://leetcode.com/problems/car-fleet/discuss/139850/C%2B%2BJavaPython-Straight-Forward

## 1710 Maximum Units On a Truck
Monday (01/08)

P: Read the question

S: Greedy solution
Sorting O(nlogn) and then traversing the array for the maximum units, O(n)
T: O(nlogn) | S: O(1)

## 378 Kth smallest element in a sorted matrix [S]
Tuesday (02/08)
Ref: https://www.techiedelight.com/find-kth-smallest-element-array/

P: Read the question

S: Using min heap
Create a min heap and remove k-1 elements. You will remain with the kth smallest element as the root.
T: O(n + k log(n))

S: Using max heap of size k
Create a max heap of size k, keep updating each element one my one while ensuring the size to always remain as k.
The root node will be the kth smallest element.
O(n log(k))

S: Using binary search
Look on leetcode to revisit the solution

## 1629 Slowest Key
Tuesday (02/08)

P: Read the question
S: Linearly traverse through the array keeping a track on the maximum duration and the corresponding lexicographically maximum key.
T: O(n) | S: O(1)

## 729 My Calendar
Wednesday (03/08)
P: Read the question

S: O(n^2) approach using brute force. O(nlogn) approach using trees.

## 39 Combination Sum
P : Read the question

S: Recursion with backtracking.

## 300 Longest Increasing Subsequence
P: Given an integer array nums, return the length of the longest strictly increasing subsequence.

S: Use DP for caching and create the solution step by step
T: O(n) | S: O(n)

## 49 Group Anagrams
Tuesday (09/08)


P: Given an list of strings. Group anagrams together.

S: Use hashmap or a dictionary for the signature of each word.
T: O(m * n)