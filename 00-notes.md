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
P: Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
S: Traverse the array, picking one number at a time from the nums array. Adding a new element to the running_sums array as sum of the last appended running_sums array value and the nums value at the current index.
T: O(n) | S: O(1) -> can be done in place