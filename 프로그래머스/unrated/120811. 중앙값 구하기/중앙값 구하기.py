def solution(array):
    array = sorted(array)
    index = len(array) // 2
    return (array[index] + array[-index-1]) / 2