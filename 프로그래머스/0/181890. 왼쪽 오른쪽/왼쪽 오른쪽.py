def solution(str_list):
    answer = []
    flag = 0
    for i in range(len(str_list)):
        if flag == 1:
            break
        if str_list[i] == "l":
            flag = 1
            answer = str_list[:i]
        if str_list[i] == "r":
            flag = 1
            answer = str_list[i+1:]
    return answer