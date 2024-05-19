def solution(myStr):
    answer = []
    for i in ["a","b","c"]:
        myStr = myStr.replace(i, " ")
    answer = myStr.split(" ")
    answer = [x for x in answer if x]
    if not answer:
        answer.append("EMPTY")
    return answer