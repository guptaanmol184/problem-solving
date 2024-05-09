# TC: O(N) + O(N)
# SC: O(1)

def get_second_largest(arr):
    if len(arr) < 2:
        return -1
    
    l = -1
    sl = -1
    if arr[0] > arr[1]:
        sl = arr[1]
        l = arr[0]
    else:
        sl = arr[0]
        l = arr[1]
    
    for i in range(2, len(arr)):
        if arr[i] > l:
            sl = l
            l = arr[i]
        elif arr[i]!= l and arr[i] > sl:
            sl = arr[i]
    
    return sl

def get_second_smallest(arr):
    if len(arr) < 2:
        return -1
    
    s = -1
    ss = -1
    if arr[0] < arr[1]:
        s = arr[0]
        ss = arr[1]
    else:
        s = arr[1]
        ss = arr[0]
    
    for i in range(2, len(arr)):
        if arr[i] < s:
            ss = s
            s = arr[i]
        elif arr[i] != s and arr[i] < ss:
            ss = arr[i]
    
    return ss


def solution(arr):
    sl = get_second_largest(arr)
    ss = get_second_smallest(arr)

    return [ss, sl]

if __name__ == '__main__':
    assert [2, 5] == solution([1,2,4,7,7,5])
    assert [-1, -1] == solution([1])
    assert [-1, -1] == solution([])
    assert [2, 8] == solution([5, 9, 8, 2, 1])
