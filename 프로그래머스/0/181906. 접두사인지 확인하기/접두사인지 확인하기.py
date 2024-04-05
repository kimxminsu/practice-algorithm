def solution(my_string, is_prefix):
    answer = 0
    prefixes = []
    for i in range(len(my_string)):
        prefixes.append(my_string[0:i])
    if is_prefix in prefixes:
        answer = 1
    return answer