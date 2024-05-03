# 소수점 반환 - / 
# 정수만 반환 - //
# 배열 추가는 append

def solution(arr):
    answer = []
    
    for array in arr:
        if array >= 50 and array % 2 == 0:
            answer.append(array // 2)  # 정수 나눗셈
        elif array < 50 and array % 2 != 0:
            answer.append(array * 2)
        else:
            answer.append(array)
    
    return answer
