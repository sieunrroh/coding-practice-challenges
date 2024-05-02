def solution(myString, pat):
    answer = 0
    
    pat_lower= pat.lower()
    myString_lower = myString.lower()
    
    if pat_lower in myString_lower:
        return 1
    else:
        return 0