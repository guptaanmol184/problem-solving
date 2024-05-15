def solution(arr):
    
    if len(arr) == 0:
        return None
    
    largest = arr[0]
    for num in arr:
        largest = max(largest, num)
    
    return largest

if __name__ == "__main__":
    assert 5 == solution([2, 5, 1, 3, 0])
    assert 10 == solution([8, 10, 5, 7, 9])
    assert None == solution([])
    print('all passed')



