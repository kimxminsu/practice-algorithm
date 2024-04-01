def solution(numLog):
    answer = ''
    for i in range(1, len(numLog)):
        value = numLog[i] - numLog[i-1]
        if value == 1:
            answer += "w"
        elif value == -1:
            answer += "s"
        elif value == 10:
            answer += "d"
        elif value == -10:
            answer += "a"
    return answer