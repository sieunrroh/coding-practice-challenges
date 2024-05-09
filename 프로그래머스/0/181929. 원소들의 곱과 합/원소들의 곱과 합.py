def solution(num_list):
  
    # 곱과 합을 계산하기 위한 초기화
    num_multi = 1  # 곱을 초기화할 때는 1을 사용
    num_sum = 0    # 합을 초기화할 때는 0을 사용

    # 리스트의 각 원소에 대하여 반복
    for i in num_list:
        num_multi *= i  # 각 원소를 곱함
        num_sum += i    # 각 원소의 합

    # 합의 제곱 계산
    num_squar = num_sum ** 2

    # 조건에 따라 결과 반환
    if num_multi < num_squar:
        return 1
    else:
        return 0


