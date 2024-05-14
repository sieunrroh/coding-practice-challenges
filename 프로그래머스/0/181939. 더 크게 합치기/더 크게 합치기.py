def solution(a, b):
    answer = 0
    
    result1 = int(str(a)+str(b))
    result2 = int(str(b)+str(a))
    if result2 > result1:
        return result2
    else:
        return result1
