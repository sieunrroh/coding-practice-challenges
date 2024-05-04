def solution(num_list):
    answer = 0
    even = 0
    odd = 0 
    
    for index, num in enumerate(num_list):
        if index % 2 == 0:
            even += num
        else:
            odd += num
    if even > odd:
        return even
    else: 
        return odd