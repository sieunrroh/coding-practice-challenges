def solution(num_list):
    num_odd = ""  # 홀수를 이어 붙일 문자열
    num_even = "" # 짝수를 이어 붙일 문자열
    
    for i in num_list:
        if i % 2 == 0:
            num_even += str(i)  # 짝수이면 num_even에 문자열로 추가
        else:
            num_odd += str(i)   # 홀수이면 num_odd에 문자열로 추가
    
    # 문자열로 이어 붙인 후 정수로 변환하고 두 수를 더함
    answer = int(num_odd) + int(num_even) if num_odd and num_even else 0
    return answer 
