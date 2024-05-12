def solution(num_list, n):
    answer = []
    
    for i in range(0,len(num_list),n): # 리스트 추가이므로, append임 
           answer.append(num_list[i]) 
    return answer


# 문자열 이어붙이기는 +=