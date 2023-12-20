def solution(numLog):
    result = ""
    alp_num = {
        1: "w",
        -1: "s",
        10: "d",
        -10: "a"
    }

    for i in range(1, len(numLog)):
        diff = numLog[i] - numLog[i - 1]
        result += alp_num[diff]

    return result