def solution(num_list, n):
    answer = []
    
    num1=num_list[n:]
    num2=num_list[:n]
    
    answer = num1+num2 
    return answer