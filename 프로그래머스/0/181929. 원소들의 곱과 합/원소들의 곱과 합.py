def solution(num_list):
    answer = 0
    product = 1
    for i in range(len(num_list)):
        product *= num_list[i]
    if product < sum(num_list) ** 2:
        answer = 1
    return answer