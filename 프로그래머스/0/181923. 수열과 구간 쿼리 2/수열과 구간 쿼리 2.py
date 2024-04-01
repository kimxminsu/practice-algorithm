import sys

def solution(arr, queries):
    answer = []
    for i in range(len(queries)):
        answer.append(sys.maxsize)
        s = queries[i][0]
        e = queries[i][1]
        k = queries[i][2]
        for j in range(s, e+1):
            if arr[j] > k and arr[j] < answer[i]:
                answer[i] = arr[j]
        if answer[i] == sys.maxsize:
            answer[i] = -1
    return answer