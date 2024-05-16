def solution(arr1, arr2):
    arr1_len = len(arr1)
    arr2_len = len(arr2)
    
    if arr1_len > arr2_len:
        return 1
    elif arr2_len > arr1_len:
        return -1
    else:
        arr1_sum = sum(arr1)
        arr2_sum = sum(arr2)
        
        if arr1_sum > arr2_sum:
            return 1
        elif arr2_sum > arr1_sum:
            return -1
        else:
            return 0

