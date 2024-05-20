def solution(arr, delete_list):
    
    new_list = [i for i in arr if i not in delete_list]
    return new_list