def solution(myString, pat):
    answer = 0
    index = myString.find(pat)
    while index != -1:
        answer += 1
        index = myString.find(pat, index + 1)
    return answer