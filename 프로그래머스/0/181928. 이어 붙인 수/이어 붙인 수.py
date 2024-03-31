def solution(num_list):
    answer = 0
    odd_concatenated = ""
    even_concatenated = ""
    for i in num_list:
        if i % 2 == 0:
            even_concatenated += str(i)
        else:
            odd_concatenated += str(i)
    answer = int(odd_concatenated) + int(even_concatenated)
    return answer