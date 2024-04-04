def solution(my_string, is_suffix):
    answer = 0
    suffixes = []
    for i in range(len(my_string)):
        suffixes.append(my_string[i:len(my_string)])
    for i in suffixes:
        if i == is_suffix:
            answer = 1
    return answer