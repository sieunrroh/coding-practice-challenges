def solution(my_strings, parts):
    answer = ''
    
    for i, (start, end) in zip(my_strings, parts):
        answer += i[start:end+1]
    
    return answer
    