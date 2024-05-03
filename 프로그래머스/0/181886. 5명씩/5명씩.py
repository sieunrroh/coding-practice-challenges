def solution(names):
    answer = []
    
    for i in range(0, len(names), 5): # i=0, i=5... 이렇게 나눠줌
        group = names[i:i+5] 
        answer.append(group[0])
    return answer