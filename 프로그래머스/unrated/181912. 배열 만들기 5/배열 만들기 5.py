def solution(intStrs, k, s, l):
    result = []

    for num_str in intStrs:
        substring = num_str[s:s + l]
        num = int(substring)
        if num > k:
            result.append(num)

    return result
