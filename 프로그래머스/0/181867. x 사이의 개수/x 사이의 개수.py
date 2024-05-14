def solution(myString):
    answer = []
    
    str = myString.split('x')
    
    answer = [len(i) for i in str]
    return answer