def solution(arr, queries):
    answer = arr
    for i in range(len(queries)):
        for j in range(len(answer)):
            if j >= queries[i][0] and j <= queries[i][1]:
                answer[j] += 1
    return answer