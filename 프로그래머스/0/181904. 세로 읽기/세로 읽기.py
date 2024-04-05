def solution(my_string, m, c):
    answer = ''
    lines = 0
    lines = len(my_string) // m
    for i in range(lines):
        answer += my_string[m * i + c - 1]
    return answer