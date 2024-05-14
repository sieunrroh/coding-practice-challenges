def solution(num_list):
    answer = []
    
    if num_list[-1] > num_list[-2]:
            num_list.append(num_list[-1] - num_list[-2]) # +=는 리스트와 리스트 결합
    else: 
            num_list.append(num_list[-1] *2)
    return num_list