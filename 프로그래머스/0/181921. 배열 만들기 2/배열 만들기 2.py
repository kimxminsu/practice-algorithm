def solution(l, r):
    answer = []
    i = 1
    while int(bin(i)[2:]) * 5 <= r:
        if int(bin(i)[2:]) * 5 >= l:
            answer.append(int(bin(i)[2:]) * 5)
        i += 1
    if not answer:
        answer.append(-1)
    return answer