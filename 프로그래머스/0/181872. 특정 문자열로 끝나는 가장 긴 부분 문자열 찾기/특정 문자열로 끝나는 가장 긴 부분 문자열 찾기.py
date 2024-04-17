def solution(myString, pat):
    answer = ''
    end_idx = myString.rfind(pat)
    answer = myString[:end_idx + len(pat)]
    return answer
