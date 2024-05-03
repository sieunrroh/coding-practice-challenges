def solution(todo_list, finished):
    answer = []
    
    for todo, fin in zip(todo_list, finished): # 동시 순회 
        
        if not fin: #false이면, 
            answer.append(todo) # false인 것만 요소 추가
    return answer