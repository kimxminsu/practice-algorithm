def solution(intStrs, k, s, l):
    answer = []
    for int_str in intStrs:
        int_str_cut = int(int_str[s:s+l])
        if int_str_cut > k:
            answer.append(int_str_cut)
    return answer