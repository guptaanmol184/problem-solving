# LC: 189 Rotate Array
# Link: https://leetcode.com/problems/rotate-array/description/

# Approach: Right rotate the array
# save the k nums in a separate array
# move the others in places
# store back the one's that were saved
# TC: O(K) + O(n)
# SC: O(k)
def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k = k % n
    k = n -k # because we are rotating left
    
    saved = nums[:k]
    for i in range(0, n-k):
        nums[i] = nums[i+k]
    for i in range(0, k):
        nums[n - k + i] = saved[i]

    return nums

# Approach 2: Using reversal of list.
# reverse complete list, then reverse individual parts of the list to set them straight
# TC: O(n) + O(n)
# SC: O(k)
def rev_list(arr):
    l = 0
    r = len(arr) - 1

    while l < r:
        tmp = arr[l]
        arr[l] = arr[r]
        arr[r] = tmp
        l+=1
        r-=1
    return arr


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        rev_nums = rev_list(nums)
        rev_nums[:k] = rev_list(nums[:k])
        rev_nums[k:] = rev_list(nums[k:])
        return rev_nums
