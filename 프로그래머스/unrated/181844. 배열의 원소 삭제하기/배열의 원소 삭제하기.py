def solution(arr, delete_list):
    answer = [j for j in arr if j not in delete_list]
    return answer