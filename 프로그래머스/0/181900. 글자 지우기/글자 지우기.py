def solution(my_string, indices):
    string_list = list(my_string)
    for i in indices:
        string_list[i] = ''
    return ''.join(string_list)
    
    # string_list = list(my_string)
    # indices.sort(reverse = True)  #내림차순 정렬
    # for i in indices:
    #     del string_list[i]
    # return ''.join(string_list)
    
    # answer = ''
    # for i in range(len(my_string)):
    #     if i not in indices:
    #         answer += my_string[i]
    # return answer