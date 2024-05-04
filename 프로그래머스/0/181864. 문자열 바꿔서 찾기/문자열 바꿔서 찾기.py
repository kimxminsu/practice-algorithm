def solution(myString, pat):
    answer = 0
    replace_myString = myString.replace("A","b").replace("B","a")
    replace_myString = replace_myString.upper()
    if pat in replace_myString:
        answer = 1
    return answer