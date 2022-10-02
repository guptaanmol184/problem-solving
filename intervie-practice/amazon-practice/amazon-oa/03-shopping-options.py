def print_all_sum(target: int) -> list:
    result = []
    output = []
    print_all_sum_rec(target, 0, 1, output, result)

    return output

def print_all_sum_rec(target, current_sum, start, output, result):
    if current_sum == target:
        output.append(result.copy())
        return
    
    for i in range(start, target):
        temp_sum = current_sum + i
        if temp_sum <= target:
            result.append(i)
            print_all_sum_rec(target, temp_sum, i, output, result)
            result.pop()
        else:
            # pop to previous stack, since continuing will only have higher values
            return
    
