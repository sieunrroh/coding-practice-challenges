def solution(numer1, denom1, numer2, denom2):
    
    bj = numer1 * denom2 + numer2 * denom1
    bm = denom1 * denom2
# 기약 분수 만들기(gcd)
    start = max(bj, bm) 
    value = 1
    
    for num in range(start, 0,  -1):
        if bj % num == 0 and bm % num == 0:
            value  = num
            break
            
# 기약 분수 찾고 난 후, 배열 반환
    answer = [bj / value, bm / value]
    return answer
    