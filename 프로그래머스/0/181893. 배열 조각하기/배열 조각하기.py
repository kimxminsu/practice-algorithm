def solution(arr, query):
    answer = arr
    for i in range(len(query)):
        if i % 2 == 0:
            answer = answer[0:query[i]+1]
        else:
            answer = answer[query[i]:]
    return answer