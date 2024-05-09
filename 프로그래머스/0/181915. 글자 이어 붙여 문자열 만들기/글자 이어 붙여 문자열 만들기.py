def solution(my_string, index_list):
    answer = ''
    
    my_string_index = [my_string[index] for index in index_list]
    answer = ''.join(my_string_index)
    return answer