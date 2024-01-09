def solution(date1, date2):
    answer = 0
    if date1 < date2:
        answer = 1
    elif date1 >= date2:
        answer = 0
    return answer