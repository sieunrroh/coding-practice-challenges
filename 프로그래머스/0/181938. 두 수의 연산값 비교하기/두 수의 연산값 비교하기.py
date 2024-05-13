def solution(a, b):
    answer = 0
    
    add = int(str(a) + str(b))
    multi = 2 * a * b
    
    if add < multi:
        return multi
    else:
        return add
