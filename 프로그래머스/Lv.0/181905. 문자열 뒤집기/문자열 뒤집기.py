def solution(my_string, s, e):
    substr = reversed(list(my_string[s:e+1]))
    return my_string[:s] + ''.join(substr) + my_string[e+1:]