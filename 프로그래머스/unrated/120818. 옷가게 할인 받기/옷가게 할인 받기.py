def solution(price):
    
    if(price >= 500000):
        discount = price * 0.2
        price -= discount
    elif(price >= 300000):
        discount = price * 0.1
        price -= discount
    elif(price >= 100000):
        discount = price * 0.05
        price -= discount
    
    return int(price)