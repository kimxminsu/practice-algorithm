def solution(a, b, c):
    answer = 0
    total_abc = a + b + c
    total_squared = a ** 2 + b ** 2 + c ** 2
    total_cubed = a ** 3 + b ** 3 + c ** 3
    if a == b and b == c:
        answer += total_abc * total_squared * total_cubed
    elif a != b and b != c and a != c:
        answer += total_abc
    else:
        answer += total_abc * total_squared
    return answer