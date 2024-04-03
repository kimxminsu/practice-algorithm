def solution(my_string, queries):
    answer = ''
    chars = list(my_string)
    for query in queries:
        start_index, end_index = query[0], query[1]
        for j in range((end_index - start_index + 1) // 2):
            temp = chars[start_index + j]
            chars[start_index + j] = chars[end_index - j]
            chars[end_index - j] = temp
    answer = ''.join(chars)
    return answer