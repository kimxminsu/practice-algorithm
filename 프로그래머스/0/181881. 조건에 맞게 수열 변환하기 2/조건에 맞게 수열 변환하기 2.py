def solution(arr):
    answer = 0
    while True:
        next_arr = []       #while문 한번 돌때마다 next_arr 초기화
        for i in arr:
            if i >= 50 and i % 2 == 0:
                next_arr.append(i // 2)
            elif i < 50 and i % 2 != 0:
                next_arr.append(i * 2 + 1)
            else:
                next_arr.append(i)
        if arr == next_arr: #arr(x) == arr(x+1)
            return answer   #while문 종료
        else:
            answer = answer + 1
            arr = next_arr