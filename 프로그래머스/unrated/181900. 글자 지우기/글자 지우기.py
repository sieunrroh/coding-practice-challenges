def solution(my_string, indices):
    result = list(my_string)
    
    for index in sorted(indices, reverse=True):
        result.pop(index)
    
    return ''.join(result)