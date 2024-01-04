def solution(arr, n):
    length = len(arr)

    for i in range(length):
        if length % 2 == 1 and i % 2 == 0:  
            arr[i] += n
        elif length % 2 == 0 and i % 2 == 1:  
            arr[i] += n

    return arr
