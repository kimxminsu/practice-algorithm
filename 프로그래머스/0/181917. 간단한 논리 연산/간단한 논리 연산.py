def solution(x1, x2, x3, x4):
    answer = True
    result1 = False if not x1 and not x2 else True
    result2 = False if not x3 and not x4 else True
    answer = True if result1 and result2 else False
    return answer