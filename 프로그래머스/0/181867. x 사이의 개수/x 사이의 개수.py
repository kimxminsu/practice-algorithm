def solution(myString):
    answer = []
    prev = 0
    split_myString = myString.split('x')
    for i in split_myString:
        answer.append(len(i))
    return answer