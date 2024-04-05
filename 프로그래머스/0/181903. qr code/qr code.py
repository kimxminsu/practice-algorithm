def solution(q, r, code):
    answer = ''
    for i in range(len(code)):
        answer += code[i] if i % q == r else ''
    return answer