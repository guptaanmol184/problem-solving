# LC: 1752: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

def check(self, nums: List[int]) -> bool:
    wrong_order_count = 0
    l = len(nums)
    for i in range(l):
        if nums[(i+1)% l] >= nums[i]:
            continue
        else:
            wrong_order_count +=1 
            if wrong_order_count > 1:
                return False
    
    return True

# Learning:
# Using module operation is powerful, since it automatically handles comparing the last element to the first element.
# Else we have to do it manually, which you thought of.

if __name__ == '__main__':
    assert True == check([1,2,3,4,5])
    assert False == check(3,4,5,1,2,4)
    assert True == check(3,4,5,12)