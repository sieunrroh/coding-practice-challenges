def solution(names):
    answer = []
      
    group_size = 5
    
    for i in range(0, len(names), group_size):
        group = names[i:i+group_size]
        answer.append(group[0])

    return answer