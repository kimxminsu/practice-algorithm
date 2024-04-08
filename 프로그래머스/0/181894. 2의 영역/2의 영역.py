def solution(arr):
    answer = []
    start_idx = -1
    end_idx = -1
    for i in range(len(arr)):
        if arr[i] == 2 and start_idx == -1:
            start_idx = i
            end_idx = start_idx
        elif arr[i] == 2 and start_idx != -1:
            end_idx = i
    answer = arr[start_idx:end_idx + 1] if start_idx != -1 else [-1]
    return answer