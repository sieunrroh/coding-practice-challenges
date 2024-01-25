def solution(i, j, k):
    answer = 0
    for e in range(i,j+1):
        answer += str(e).count(str(k))
    return answer