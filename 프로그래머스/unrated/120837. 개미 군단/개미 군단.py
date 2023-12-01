def solution(hp):
    count = 0
    ants = [5,3,1]
    
    for att in ants:
        count += hp // att
        hp %= att
    return count