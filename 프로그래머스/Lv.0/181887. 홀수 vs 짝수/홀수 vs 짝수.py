def solution(num_list):
    odd_sum = 0
    even_sum = 0

    for i, num in enumerate(num_list, start=1):
        if i % 2 == 1:
            odd_sum += num
        else:
            even_sum += num

    return max(odd_sum, even_sum)
