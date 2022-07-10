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