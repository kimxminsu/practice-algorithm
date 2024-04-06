def solution(my_string):
    answer = []
    for i in range(52): #A~Z...a~z
        answer.append(0)
    for i in my_string:
        if i < 'a':
            answer[ord(i) - ord('A')] += 1
        else:
            answer[ord(i) - ord('a') + len(answer) // 2] += 1
    return answer