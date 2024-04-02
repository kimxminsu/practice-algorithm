def solution(start_num, end_num):
    answer = []
    for i in range(0, end_num - start_num + 1):
        answer.append(i + start_num)
    return answer