def solution(num_list):
    answer = 0
    odd_total = 0
    even_total = 0
    for i in range(len(num_list)):
        if (i+1) % 2 == 0:
            even_total += num_list[i]
        else:
            odd_total += num_list[i]
    if odd_total > even_total:
        answer = odd_total
    else:
        answer = even_total
    return answer