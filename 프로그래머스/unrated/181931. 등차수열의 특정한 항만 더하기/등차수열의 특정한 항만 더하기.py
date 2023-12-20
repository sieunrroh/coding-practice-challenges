def solution(a, d, included):
    total_sum = 0
    current_term = a

    for i in range(len(included)):
        if included[i]:
            total_sum += current_term
        current_term +=d

    return total_sum