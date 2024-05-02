def solution(strArr):
    answer = []
    
    
    # 원소 반복, index와 원소 둘다
    # 파이썬에서 += 연산자는 리스트에 다른 리스트를 연결할 때 주로 사용
    # append는 요소 추가
    for index, str in enumerate(strArr):
        if index % 2 == 0:
            answer.append(str.lower())
        else:
            answer.append(str.upper())
        
    return answer