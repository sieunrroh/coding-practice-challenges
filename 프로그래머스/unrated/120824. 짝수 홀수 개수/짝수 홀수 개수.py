def solution(num_list):
    answer = []
    even_n, odd_n = 0,0
    
    for num in num_list:
        if num % 2 == 0:
            even_n +=1
        else: 
            odd_n += 1
            
    answer = [even_n, odd_n]
    return answer