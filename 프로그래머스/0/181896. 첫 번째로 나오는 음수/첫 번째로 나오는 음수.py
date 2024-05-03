def solution(num_list):
    answer = 0
    
    for index, i in enumerate(num_list):
        if i < 0:
            return index
    return -1 # for문을 다 돌아도 없으니 for문에서 빠져나와 -1 반환
    