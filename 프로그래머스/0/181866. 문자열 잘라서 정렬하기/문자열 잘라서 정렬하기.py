def solution(myString):
   
    str = myString.split('x')
    str = [i for i in str if i]
    str.sort()
    return str