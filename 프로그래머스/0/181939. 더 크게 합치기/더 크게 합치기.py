def solution(a, b):
    answer = 0
    # if int(str(a) + str(b)) < int(str(b) + str(a)):
    #     answer = int(str(b) + str(a))
    # else:
    #     answer = int(str(a) + str(b))
    answer = int(max(f"{a}{b}", f"{b}{a}"))
    return answer