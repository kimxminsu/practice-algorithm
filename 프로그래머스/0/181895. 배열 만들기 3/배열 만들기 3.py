def solution(arr, intervals):
    answer = []
    answer += arr[intervals[0][0]:intervals[0][1]+1]    #first_list
    answer += arr[intervals[1][0]:intervals[1][1]+1]    #second_list
    return answer