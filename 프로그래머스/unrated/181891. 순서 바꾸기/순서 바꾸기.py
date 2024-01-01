def solution(num_list, n):
    if n >= len(num_list):
        return num_list
    
    split_list = num_list[n:]
    split_list.extend(num_list[:n])
    
    return split_list