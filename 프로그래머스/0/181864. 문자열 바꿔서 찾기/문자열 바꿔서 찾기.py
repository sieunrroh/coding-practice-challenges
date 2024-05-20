def solution(myString, pat):
    answer = 0
    transformed = ''.join(['B' if char == 'A' else 'A' for char in myString])
    
    # 패턴이 포함되어 있는지 확인
    if pat in transformed:
        return 1
    else:
        return 0
    return answer