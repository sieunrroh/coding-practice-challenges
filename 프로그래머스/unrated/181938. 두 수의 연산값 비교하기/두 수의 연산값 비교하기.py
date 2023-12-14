def solution(a, b):
    answer1 = ''
    answer1 = str(a) + str(b)
    answer1 = int(answer1)
                 
                 
    answer2 = 2 * a * b
    if answer1 > answer2: 
        return answer1
    else:
        return answer2
        